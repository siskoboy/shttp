from shttp.methods import HTTPResponse as response
from shttp.methods import HTTPRequest as request
from shttp.networking import connection
from shttp.parse import parser as reqparser

from os import fork
from signal import signal, SIGCHLD, SIG_IGN, SIG_INT, SIG_HUP
from sys import exit

# TODO proper argparser
# TODO sighandlers CHLD, INT, HUP

socketio = connection('127.0.0.1', 8081)

while True:
   socketio.accept()
   pid = fork()

   if pid == 0:
      # recv and parse requeset
      data = socketio.recv_request()
      req = reqparser.parse(data)

      # build and transmit response
      resp = response(req)
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

