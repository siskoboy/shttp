from datetime import datetime
from os import stat

class HTTPRequest:
   def __init__(self, method, url, proto, headers):
      self.method = method
      self.url = url
      self.proto = proto
      self.headers = headers

   def __str__(self):
      return str({
         'METHOD':   self.method,
         'URL':      self.url,
         'PROTO':    self.proto,
         'HEADERS':  self.headers,
      })



class HTTPResponse:
   # _status_line
   # _headers
   # _content

   # _cname

   #rfc-2616
   _code_desc = {
      200: 'OK',
      400: 'Bad Request',
      403: 'Forbidden',
      404: 'Not Found',
      405: 'Method Not Allowed',
      501: 'Not Implemented',
   }

   _mime_types = {
      'css':  'text/css',
      'gif':  'image/gif',
      'html': 'text/html',
      'jpg':  'image/jpeg',
      'png':  'image/png',
   }


   def __init__(self, req, docroot):
      # common headers
      self._headers = {
         'Server':   'shitty-p 1.0',
         'Date':     datetime.now().strftime('%d %b %Y %H:%M:%S'),
      }

      # TODO not the best place for logging!!
      print "%s %s" % (req.method, req.url)

      if req.method == 'HEAD':
         self._include_content = False
      else:
         self._include_content = True

      # known failure cases
      if not req:
         self._setup_4XX(400)
      elif req.proto == 'HTTP/1.1' and not req.headers.has_key('Host'):
         self._setup_4XX(400)
      elif req.method not in ('GET', 'HEAD'):
         self._setup_5XX(501)

      # check for file existence
      #  stat() asserts OSError when file does not exist
      #  open() asserts IOError on E_NOPERM
      self._cname = self._canonicalize_name(req.url)
      try:
         st = stat('%s/%s' % (docroot, self._cname))
         fd = open('%s/%s' % (docroot, self._cname), 'r')

         self._content = fd.read(st.st_size)
         fd.close()
         self._setup_2XX(200)
      except OSError:
         self._setup_4XX(404)
      except IOError:
         self._setup_4XX(403)


   # HTTP 2XX handler
   def _setup_2XX(self, code):
      self._status_line = 'HTTP/1.1 %d %s' % (code, self._code_desc[code])
      self._headers['Content-Type'] = self._mimetype(self._cname)
      self._headers['Content-Length'] = len(self._content)


   # HTTP 4XX handler
   def _setup_4XX(self, code):
      self._status_line = 'HTTP/1.1 %d %s' % (code, self._code_desc[code])
      self._content = '<html><body><h1>%d %s</body></html>' % (code, self._code_desc[code])
      self._headers['Content-Type'] = 'text/html'
      self._headers['Content-Length'] = len(self._content)


   # HTTP 5XX handler
   def _setup_5XX(self,code):
      self._status_line = 'HTTP/1.1 %d %s' % (code, self._code_desc[code])
      self._content = '<html><body><h1>%d %s</body></html>' % (code, self._code_desc[code])
      self._headers['Content-Type'] = 'text/html'
      self._headers['Content-Length'] = len(self._content)


   # craft a formatted HTTP response
   def format_resp(self):
      s = self._status_line + '\r\n'

      for n in self._headers:
         s += '%s: %s\r\n' % (n, self._headers[n])
      s += '\r\n'

      # in the case of HEAD, we must not transmit content
      if self._content and self._include_content:
         s += self._content

      return s


   # generate a canonicalized name from the requested resource
   def _canonicalize_name(self, url):
      cname = ['',]

      # strip off the leading <scheme://add.re.ss[:port]>
      schemeloc = url.rfind('://')
      if schemeloc != -1:
         # schmemloc+3 would be the index of the scheme://
         url = url[schemeloc+3:]
         pathloc = url.find('/')
         if pathloc != -1:
            url = url[pathloc:]
         else:
            url = '/'

      # use a stack to walk the url and canonicalize the name to the relative
      # root of /.
      for n in url.split('/'):
         if n == '..':
            cname.pop()
            if not cname:
               cname.append('')
         elif n == '.' or n == '':
            pass
         else:
            cname.append(n)

      return '/'.join(cname)



   def _mimetype(self, cname):
      idx = cname.find('.')
      if idx == -1:
         return 'text/html'
      else:
         return self._mime_types[cname[idx+1:]]
