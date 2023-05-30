#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open a socket and listen for HTTP requests
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    
    # Accept a connection and make a connection to the server
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from', client_address)
        
        # Receive the request and decode it
        request = connection.recv(1024)
        request = request.decode()
        
        # Send the response to the client
        connection.sendall(request)
        
        # Close the connection
        connection.close()
        
        # Append the decoded request to the list of words
        words.append(request)
        
        # Send the response to the client
        connection.sendall(','.join(words))
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('\n')
        
        # Close the connection
        connection.close()
        
        # Send the response to the client
        connection.sendall('