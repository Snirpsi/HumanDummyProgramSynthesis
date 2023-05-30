#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import os
    import socket
    
    HOST, PORT = 'localhost', 8080
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while True:
        connection, address = sock.accept()
        print('Connected by', address)
        
        while True:
            data = connection.recv(1024)
            if not data: break
            connection.sendall(data)
        
        connection.close()
        
