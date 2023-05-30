#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and calculates user input. """    
    port = sys.argv[1]
    
    # Open a socket to listen on the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    
    # Accept a connection
    client, addr = sock.accept()
    
    # Print the port number
    print('Port {} is listening on {}'.format(port, addr))
    
    # Print the IP address of the client
    print('Client IP: {}'.format(addr))
    
    # Send a message to the client
    client.send('Hello World!')
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
