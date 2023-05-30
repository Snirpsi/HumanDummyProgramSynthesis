#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and converts all ports. """    
    
    ports = []
    
    # Open a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(10)
    
    # Accept connections.
    while True:
        connection, client_address = server_socket.accept()
        
        # Accept a request for port 8080 and convert it to an integer.
        request = connection.recv(1024).decode()
        
        # Convert port 8080 to an integer.
        port = int(request)
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        
        # Send the port number to the client.
        connection.send(str(port))
        
        # Close the connection.
        connection.close()
        