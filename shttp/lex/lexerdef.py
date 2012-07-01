tokens = (
   'METHOD',
   'URL',
   'PROTO',
   'HEADER',
   'HVAL',
)

states = (
   #('lexmethod','exclusive'),
   ('lexurl','exclusive'),
   ('lexproto','exclusive'),
   ('lexheader','exclusive'),
   ('lexhval','exclusive'),
)

# per rfc-3986
#gen-delims = r'[:/?#\[\]@]'
#sub-delims = r'[!$&\'()*+,;=]'
#unreserved = r'[\w\d._~-]'

def t_INITIAL_METHOD(t):
   r'(HEAD|GET|OPTIONS)'
   t.lexer.begin('lexurl')
   return t

def t_lexurl_URL(t):
   r'[:/?#\[\]@!$&\'()*+,;=\w\d._~-]+'
   t.lexer.begin('lexproto')
   return t

def t_lexproto_PROTO(t):
   r'HTTP/1.[01]'
   t.lexer.begin('lexheader')
   return t

#t_lexheader_ignore = ':'
def t_lexheader_HEADER(t):
   r'[\w\d:-]+'
   t.lexer.begin('lexhval')
   return t

def t_lexhval_HVAL(t):
   r'[^\r]+'
   t.lexer.begin('lexheader')
   return t

def t_ANY_newline(t):
   r'\r\n'
   t.lexer.lineno += len(t.value)

t_ANY_ignore = ' \t'

def t_ANY_error(t):
   print "Illegal Character '%s'" % t.value[0]
   t.lexer.skip(1)


