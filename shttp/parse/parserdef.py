from ..lex.lexerdef import tokens
from ..methods import HTTPRequest as req

_headers = {}
def p_req(p):
   'request : reqstr ENDL headers ENDL'
   #p[0] = {
   #   'METHOD':  p[1][0],
   #   'URL':     p[1][1],
   #   'PROTO':   p[1][2],
   #   'HEADERS': _headers,
   #}
   p[0] = req(p[1]['METHOD'], p[1]['URL'], p[1]['PROTO'], _headers)

def p_reqstr(p):
   'reqstr : METHOD URL PROTO'
   p[0] = {
      'METHOD': p[1],
      'URL':    p[2],
      'PROTO':  p[3],
   }

def p_headers(p):
   '''headers : aheader headers
              | empty'''
   pass

def p_aheader(p):
   'aheader : HEADER HVAL ENDL'
   _headers[p[1].rstrip(':')] = p[2]

def p_empty(p):
   'empty :'
   pass

def p_error(p):
   #print "Parse Error!!"
   pass

