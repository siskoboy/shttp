import socket

class connection:
   def __init__(self, host, port):
      self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self._s.bind((host,port))
      self._s.listen(1)

   def accept(self):
      conn, addr = self._s.accept()
      return conn, addr

   def close(self):
      self._s.close()
