#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    
    ports = []
    
    # Get the ports
    ports = socket.getservbyname('http', 'https')
    
    # Print the ports
    for port in ports:
        print('http', port)
    
    # Close the socket
    socket.close()
    
