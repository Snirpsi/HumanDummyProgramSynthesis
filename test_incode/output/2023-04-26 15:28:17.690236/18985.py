#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    import os
    import socket
    import sys
    
    HOST, PORT = "localhost", 8000
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    
    while True:
        client, address = server.accept()
        print("Got connection from ", address)
        
        buf = client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
            break
        
        buf += client.recv(1024)
        if not buf:
