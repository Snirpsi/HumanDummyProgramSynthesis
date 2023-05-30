#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports. """    
    ports = []
    
    ports.append( get_port( 0 ) )
    ports.append( get_port( 1 ) )
    ports.append( get_port( 2 ) )
    
    for port in ports:
        print( port )
        
    
<|/ file source=github ext=.py |>