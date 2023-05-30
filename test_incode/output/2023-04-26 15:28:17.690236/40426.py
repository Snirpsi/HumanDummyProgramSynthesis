#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or removes a port. """    
    
    # Print all ports
    ports = list( enumerate( sys.stdin ) )
    for port in ports:
        sys.stdout.write( port[1] )
        sys.stdout.flush()
    
    # Remove a port
    ports.remove( 0 )
    
    # Print all ports
    for port in ports:
        sys.stdout.write( port[1] )
        sys.stdout.flush()
    
    
