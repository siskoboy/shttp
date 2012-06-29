import ply.yacc as yacc
from .parserdef import *

if __name__ != '__main__':
   parser = yacc.yacc(debug=0, outputdir='shttp/parse/')
