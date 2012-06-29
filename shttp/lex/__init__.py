from .lexerdef import *
import ply.lex as lex

# ply parser generator assumes the existence of lex.lexer
# (e.g. from lex import lexer)
if __name__ != '__main__':
   lexer = lex.lex()

