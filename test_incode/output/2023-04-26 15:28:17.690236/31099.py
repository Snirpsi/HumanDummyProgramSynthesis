#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    port = int(sys.argv[1])
    
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    
    # Create a client socket
    client_socket, client_address = server_socket.accept()
    
    # Print the port number
    print('The port number is:', port)
    
    # Close the sockets
    client_socket.close()
    server_socket.close()
    
