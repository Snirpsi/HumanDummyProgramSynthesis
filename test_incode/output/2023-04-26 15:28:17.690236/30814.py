#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and opens a list of numbers. """    
    
    import sys
    import socket
    
    HOST = 'localhost'
    PORT = 8080
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        
        data = conn.recv(1024)
        
        print('Received', repr(data))
        
        conn.sendall('