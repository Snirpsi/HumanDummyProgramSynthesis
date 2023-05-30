#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    # Open a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(10)
    
    # Listen for connections.
    while True:
        connection, client_address = server_socket.accept()
        
        # Receive the request from the client.
        data = connection.recv(1024)
        
        # Send the response to the client.
        connection.send('HTTP/1.1 200 OK\r\nServer: Words\r\nContent-Type: text/plain\r\n\r\n'.encode())
        
        # Send the response to the client.
        connection.send(''.encode())
        
        # Close the connection.
        connection.close()
