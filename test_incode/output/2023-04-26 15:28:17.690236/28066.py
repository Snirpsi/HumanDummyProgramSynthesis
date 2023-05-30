#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    import os
    import socket
    import sys
    
    HOST, PORT = "localhost", 8080
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        print("Connection from", client_address)
        
        while True:
            data = connection.recv(1024)
            if not data:
                break
            sys.stdout.write(data)
            sys.stdout.flush()
        
        connection.close()
        
    server_socket.close()
    
