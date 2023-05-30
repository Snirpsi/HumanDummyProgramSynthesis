#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    # Open a port and listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    
    # Accept a connection from the client.
    client, client_address = server_socket.accept()
    
    # Receive the message and print it.
    message = client.recv(1024)
    print(message)
    
    # Close the socket and quit.
    client.close()
    server_socket.close()
    
