#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    
    # Get the list of ports
    ports = list( enumerate( socket.getservbyname('http') ) )
    
    # Print the list of ports
    for port in ports:
        print( 'Port {} is {}'.format( port[0], port[1] ) )
    
    # Close the socket and quit the program
    socket.close( 