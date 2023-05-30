#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import os
    import socket
    import sys
    
    HOST, PORT = "localhost", 9999
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    
    while True:
        connection, address = server.accept()
        print("Got connection from %s" % address)
        
        connection.sendall("GET / HTTP/1.0\r\n\r\n")
        
        connection.close()
    
