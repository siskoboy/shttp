import socket

class connection:
   # _serv_socket
   # _cli_socket
   # _cli_addr

   def __init__(self, host, port):
      self._serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self._serv_socket.bind((host,port))
      self._serv_socket.listen(1)

   def accept(self):
      self._cli_socket, self._cli_addr = self._serv_socket.accept()

   # close a client socket
   def close(self):
      self._cli_socket.close()

   # close the server socket
   def shutdown(self):
      self._serv_socket.close()

   # utility functions to get information about the client
   def get_cli_addr(self):
      return self._cli_addr[0]
   def get_cli_port(self):
      return self._cli_addr[1]

