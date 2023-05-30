#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    import os
    import socket
    
    HOST, PORT = 'localhost', 8080
    
    # Create a socket to listen on
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    sock.bind((HOST, PORT))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection
    conn, addr = sock.accept()
    
    # Receive the file from the client
    data = conn.recv(1024)
    
    # Send the file back to the client
    conn.send(data)
    
    # Close the connection
    conn.close()
    
    # Close the socket
    sock.close()
    
    print('Server running at http://%s:%s/fruits.html' % (HOST, PORT))
    
