from datetime import datetime

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
   # _response_str
   # _headers
   # _content
   def __init__(self, req):
      if not req:
         self._setup_400()
      elif req.proto == 'HTTP/1.1' and not req.headers.has_key('Host'):
        self._setup_400()

      # TODO remove
      self._setup_400()

   def _setup_400(self):
      self._response_str = 'HTTP/1.1 400 BAD REQUEST'
      self._content = '<html><body><h1>400 BAD REQUEST!!</body></html>'
      self._headers = {
         'Content-Type':   'text/html',
         'Content-Length': len(self._content),
         'Date':           datetime.now().strftime('%d %b %Y %H:%M:%S'),
         'Server':         'shittyp v1.0',
      }

   def DEBUG_pr_resp(self):
      print self._response_str
      for n in self._headers.keys():
         print "%s: %s" % (n, self._headers[n])
      print self._content

