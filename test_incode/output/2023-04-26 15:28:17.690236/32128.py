#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and opens words. """    
    
    # Open the port and enumerate all ports
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))
    server_socket.listen(1)
    
    # Enumerate all ports
    while True:
        server_socket.settimeout(1)
        
        # Accept a connection
        client_socket, address = server_socket.accept()
        
        # Open a connection to the word
        client_socket.connect((address, 0))
        
        # Print the word and close the connection
        client_socket.send('Hello, world!')
        client_socket.close()
        
        # Sleep for a second and repeat
        time.sleep(