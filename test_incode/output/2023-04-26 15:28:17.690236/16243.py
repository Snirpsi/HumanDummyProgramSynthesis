#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or returns words. """    
    import sys
    import socket
    
    HOST, PORT = 'localhost', 8080
    
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind((HOST, PORT))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection
    conn, addr = sock.accept()
    
    # Receive a request from the client
    request = conn.recv(1024)
    
    # Send the response back to the client
    conn.send(request