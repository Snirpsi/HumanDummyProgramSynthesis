#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or stores all ports. """    
    port = int(sys.argv[1])
    
    # Open a socket and listen on all available ports
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(10)
    
    # Accept connection and store it in list
    connections = []
    while True:
        connection, client_address = server_socket.accept()
        connections.append(connection)
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the connection
        connection.close()
        
        # Send a response to the client
        for connection in connections:
            connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the socket
        server_socket.close()
        
        # Wait for a new connection
        connection, client_address = server_socket.accept()
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the connection
        connection.close()
        
        # Send a response to the client
        for connection in connections:
            connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the socket
        server_socket.close()
        
        # Wait for a new connection
        connection, client_address = server_socket.accept()
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the connection
        connection.close()
        
        # Wait for a new connection
        connection, client_address = server_socket.accept()
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the connection
        connection.close()
        
        # Wait for a new connection
        connection, client_address = server_socket.accept()
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the connection
        connection.close()
        
        # Wait for a new connection
        connection, client_address = server_socket.accept()
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: Python\r\n\r\nHello World!\n')
        
        # Close the connection
        connection.close()
        
        # Wait for a new connection
        connection, client_address = server_socket.accept()
        
        # Handle incoming data
        connection.send('HTTP/1.1 200 OK\r\nServer: 