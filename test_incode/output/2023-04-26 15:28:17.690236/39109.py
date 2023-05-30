#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import os
    import socket
    import sys
    
    HOST, PORT = "localhost", 8080
    
    # Create a socket to listen on port 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    # Accept the connection and print its 