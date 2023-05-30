#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open a socket to listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(10)
    
    # Accept a connection from the client
    connection, client_address = server_socket.accept()
    
    # Receive the file contents and decode it into UTF-8
    bytes_data = connection.recv(1024).decode('utf-8')
    
    # Send the file contents back to the client
    connection.sendall(bytes_data)
    
    # Close the connection
    connection.close()
    
    # Send the list of words to the client
    connection.sendall('\n'.join(words))
    
    # Close the connection
    connection.close()
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words to the client
    print('\n'.join(words))
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket