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

import socket
from ..methods import HTTPResponse as response

class connection:
   # _serv_socket
   # _cli_socket
   # _cli_addr
   # _req_buffsz

   def __init__(self, host, port):
      self._serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self._serv_socket.bind((host,port))
      self._serv_socket.listen(1)
      self._buffsz = 2048

   def accept(self):
      self._cli_socket, self._cli_addr = self._serv_socket.accept()

   # close a client socket
   def close(self):
      self._cli_socket.close()

   # close the server socket
   def shutdown(self):
      self._serv_socket.close()

   # utility functions to get information about the client
   #def get_cli_addr(self):
   #   return self._cli_addr[0]
   #def get_cli_port(self):
   #   return self._cli_addr[1]

   # grab a request
   def recv_request(self):
      s = self._cli_socket.recv(self._buffsz)
      return s

   # send the response
   def send_response(self, resp):
      return self._cli_socket.send(resp.format_resp())




