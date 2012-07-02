from shttp.methods import HTTPResponse as response
from shttp.methods import HTTPRequest as request
from shttp.networking import connection
from shttp.parse import parser as reqparser

from os import fork
from signal import signal, SIG_IGN, SIGCHLD, SIGINT, SIGHUP
from sys import exit

# TODO proper argparser
# TODO sighandlers CHLD, INT, HUP

socketio = connection('127.0.0.1', 8081)
docroot = '/var/www/html'

while True:
   socketio.accept()
   pid = fork()

   if pid == 0:
      # recv and parse requeset
      data = socketio.recv_request()
      req = reqparser.parse(data)

      # build and transmit response
      resp = response(req,docroot)
      socketio.send_response(resp)

      # close client connection
      socketio.close()
      exit()
   else:
      socketio.close()

# shut down the server socket and exit
socketio.close()
socketio.shutdown()
exit()

