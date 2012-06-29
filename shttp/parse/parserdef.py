from ..lex.lexerdef import tokens

_headers = {}
def p_req(p):
   'request : reqstr headers'
   p[0] = {
      'METHOD':  p[1][0],
      'URL':     p[1][1],
      'PROTO':   p[1][2],
      'HEADERS': _headers,
   }

def p_reqstr(p):
   'reqstr : METHOD URL PROTO'
   p[0] = [p[1], p[2], p[3]]

def p_headers(p):
   '''headers : aheader headers
               | empty'''
   pass

def p_aheader(p):
   'aheader : HEADER HVAL'
   _headers[p[1].rstrip(':')] = p[2]

def p_empty(p):
   'empty :'
   pass

def p_error(p):
   print "Parse Error!!"

