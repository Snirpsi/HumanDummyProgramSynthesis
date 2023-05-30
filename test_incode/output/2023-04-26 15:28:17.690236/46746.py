#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports and enumerates a port. """    
    
    # Open the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    
    # Get the port number
    sock, port = sock.accept()
    
    # Get the port number
    sock.close()
    
    # Print the port number
    print('Port number:', port)
    
    # Close the port
    sock.close()
    
    # Close the socket
    sock.close()
    
    # Close the server
    server.close()
    
    # Close the client
    