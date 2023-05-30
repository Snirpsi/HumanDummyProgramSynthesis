#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports. """    
    
    ports = []
    
    ports.append( get_port( 0, 0 ) )
    ports.append( get_port( 1, 1 ) )
    ports.append( get_port( 2, 2 ) )
    ports.append( get_port( 3, 3 ) )
    
    for port in ports:
        print( 'Port {}: {}'.format( port, get_port_info( port ) ) )
    
