#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or returns numbers. """    
    
    port = int(sys.argv[1])
    
    # Open a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    
    # Accept a connection and then start processing it.
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from ', client_address)
        
        # Start processing data sent by the client.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')
        print(response)
        
        # Close the connection.
        connection.close()
        
        # Wait for a new client to connect.
        connection.send(b'GET / HTTP/1.0\r\n\r\n')
        
        # Receive the response and print it.
        response = connection.recv(1024).decode('utf-8')