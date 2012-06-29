from shttp.parse import parser
from shttp.netcfg import connection

shortdata = 'HEAD /index.html HTTP/1.1\r\nHost: example.com\r\nXss-forward: Yes\r\n\r\n'
longdata = 'GET /dumprequest HTTP/1.1\r\nHost: djce.org.uk\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nReferer: http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CFwQFjAB&url=http%3A%2F%2Fdjce.org.uk%2Fdumprequest&ei=a1btT_GrIKaE2wWcwriiCg&usg=AFQjCNEeAn5wSZMp_y_oTmOKonq482sS9A\r\nAccept-Encoding: gzip,deflate,sdch\r\nAccept-Language: en-US,en;q=0.8\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n\r\n'

#result = parser.parse(longdata)
result = parser.parse(shortdata)
print result

server = connection('127.0.0.1', 8080)
# todo next - sockets obj
# read request from client
# parse and stat file
# build response obj
# send
# logging
# redirect
# vhosts def's
