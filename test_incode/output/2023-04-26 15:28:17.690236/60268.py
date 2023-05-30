#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    
    # Accept connections
    while True:
        connection, client_address = server_socket.accept()
        
        # Receive the request from the client
        data = connection.recv(1024)
        
        # Send the response to the client
        connection.sendall(b'HTTP/1.1 200 OK\r\n')
        connection.sendall(b'Content-Type: text/plain\r\n')
        connection.sendall(b'\r\n')
        connection.sendall(b'