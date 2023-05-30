#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and calculates user input. """    
    
    ports = []
    
    # Start a server
    server = HTTPServer(('', 8080), Handler)
    
    # Start a client and wait for it to connect
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # Wait for client to connect
    client_socket.send('GET / HTTP/1.0\r\n\r\n')
    
    # Receive the response and store it
    response_data = client_socket.recv(1024)
    
    # Close the socket
    client_socket.close()
    
    # Print the response
    print(response_data)
    
    # Close the server
    server.socket.close()
    
    # Close the client
    client_socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the client
    client_socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the server
