#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    ports = []
    
    # Start a server
    server = HTTPServer(("", 0), MyHandler)
    
    # Start a client that connects to the server
    client_socket = socket.socket()
    client_socket.connect(("", 0))
    
    # Wait for connection
    client_socket.send("GET / HTTP/1.0\r\n\r\n")
    
    # Receive the response and store it
    response_body = client_socket.recv(4096)
    
    # Close the connection
    client_socket.close()
    
    # Print the response body
    print(response_body)
    
    # Close the server
    server.shutdown()
    
    # Close the client
    client_socket.close()
    
    # Print the server port
    print(server.server_port)
    
    # Close the server
    server.server_close()
    
    # Close the client
    client_socket.close()
    
    # Print the client port
    print(client_socket.