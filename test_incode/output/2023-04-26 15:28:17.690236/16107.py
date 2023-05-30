#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and removes words. """    
    
    import os
    import socket
    import sys
    
    HOST, PORT = "localhost", 8000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        
        data = connection.recv(1024).decode()
        
        if data:
            words = data.split()
            
            for word in words:
                if word not in ["quit", "exit"]:
                    connection.send(word.upper())
            
            connection.close()
        else:
            connection.close()
            
    server_socket.close()
    
