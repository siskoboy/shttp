from shttp.methods import HTTPResponse as response
from shttp.methods import HTTPRequest as request
from shttp.networking import connection
from shttp.parse import parser as reqparser

from argparse import ArgumentParser
from os import fork
from signal import signal, SIG_IGN, SIGCHLD, SIGINT, SIGHUP
from sys import exit

# TODO proper argparser
# TODO sighandlers CHLD, INT, HUP

argparser = ArgumentParser()
argparser.add_argument('-r', '--docroot', default='/var/www/html',
   metavar='dir', help='Site docroot')
argparser.add_argument('-l', '--listen', default='0.0.0.0',
   metavar='addr', help='Address to listen on')
argparser.add_argument('-p', '--port', default='80', type=int,
   metavar='port', help='Port to listen on')

args = argparser.parse_args()

socketio = connection(args.listen, args.port)

while True:
   socketio.accept()
   pid = fork()

   if pid == 0:
      # recv and parse requeset
      data = socketio.recv_request()
      req = reqparser.parse(data)

      # build and transmit response
      resp = response(req,args.docroot)
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

