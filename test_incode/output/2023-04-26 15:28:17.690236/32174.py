#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = []
    
    # Open a socket and listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    
    # Accept a connection and print its contents.
    while True:
        connection, client_address = server_socket.accept()
        
        # Receive the request and print it.
        data = connection.recv(1024)
        
        # Send the response back to the client.
        connection.sendall(data)
        
        # Close the connection.
        connection.close()
        
        # Add the word to the list of words.
        words.append(data.decode('utf-8'))
        
        # Close the connection.
        connection.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print the list of words back to the client.
        connection.sendall(json.dumps(words))
        
        # Close the connection.
        connection.close()
        
        # Close the socket.
        server_socket.close()
        
        # Print 