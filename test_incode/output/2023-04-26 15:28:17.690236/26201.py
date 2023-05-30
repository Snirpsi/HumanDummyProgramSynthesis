#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Open a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8080))
    server_socket.listen(1)
    
    # Accept a connection and print its contents.
    while True:
        connection, client_address = server_socket.accept()
        
        # Receive the request and print it.
        data = connection.recv(1024).decode()
        
        # Send the response back to the client.
        connection.sendall('HTTP/1.1 200 OK\r\n' +
                           'Content-Type: text/plain\r\n' +
                           'Content-Length: ' + str(len(data)) + '\r\n' +
                           '\r\n' + data)
        
        # Close the connection.
        connection.close()
        
        # Append the word to the list.
        words.append(data)
    
    # Close the socket.
    server_socket.close()
    
    # Join the words together and print them.
    print(''.join(words))
    
