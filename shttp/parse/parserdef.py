# Copyright (C) 2012 Sam Hansen
#
# This file is part of shttp
#
# shttp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# shttp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with shttp.  If not, see <http://www.gnu.org/licenses/>.

from ..lex.lexerdef import tokens
from ..methods import HTTPRequest as req

_headers = {}
def p_req(p):
   'request : reqstr CRLF headers CRLF'
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
   'aheader : HEADER HVAL CRLF'
   _headers[p[1].rstrip(':')] = p[2]

def p_empty(p):
   'empty :'
   pass

def p_error(p):
   #print "Parse Error!!"
   pass

