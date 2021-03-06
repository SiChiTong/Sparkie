# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module ...

__author__ = "Magnus Kvendseth Øye"
__copyright__ = "Copyright 2020, Sparkie Quadruped Robot"
__credits__ = ["Magnus Kvendseth Øye", "Petter Drønnen", "Vegard Solheim"]
__version__ = "1.0.0"
__license__ = "MIT"
__maintainer__ = "Magnus Kvendseth Øye"
__email__ = "magnus.oye@gmail.com"
__status__ = "Development"
"""

# Import packages
import socket
from threading import Thread


class Server(Thread):
    """doc"""

    __slots__ = ['host', 'port']

    def __init__(self, host='0.0.0.0', port=8089):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        print(self.port)
        print(self.host)
        self.connection = None
        self.content = None
    
    def run(self):
        """doc"""
        self.initialize()
        while True:
            while self.isConnected():
                self.read()
            self.content = None
    
    def close(self):
        """doc"""
        self.connection.close()
    
    def read(self):
        """doc"""
        if self.connection is not None:
            self.content = self.connection.recv(4096).decode('latin-1')
    
    def send(self, msg):
        """doc"""
        print("Sending")
        self.connection.send(msg.encode())
            
            
    def initialize(self):
        """doc"""
        addr = (self.host, self.port)
        self.socket.bind(addr)
        self.socket.listen(100)
        self.connection, self.address = self.socket.accept()
        print('Connected by', self.address)
    
    def listening(self):
        print('Waiting for a connection...')
        self.connection, self.address = self.socket.accept()
        print('Connected by', self.address)
        
    
    def disconnect(self):
        """doc"""
        self.connection.close()
        self.connection = None
    
    def isConnected(self):
        """doc"""
        return self.connection is not None
    

# Example of usage
if __name__ == "__main__":
    server = Server(host='0.0.0.0', port=8089)
    #server.start()
    server.initialize()
    while server.isConnected():
        print(server.read())
        server.send("Hello")