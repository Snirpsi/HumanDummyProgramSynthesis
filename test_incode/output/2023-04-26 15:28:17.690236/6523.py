#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    import sys
    import socket
    
    HOST, PORT = 'localhost', 8080
    
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = ('', PORT)
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection
    print('Waiting for connection...')
    connection, client_address = sock.accept()
    
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.sendall(data)
    
    # Close the connection
    connection.close()
    
    # 