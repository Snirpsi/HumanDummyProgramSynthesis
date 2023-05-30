#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or returns all ports. """    
    ports = []
    while True:
        ports.append( get_port() )
        sleep( 1 )
    
    
<|/ file source=github filename=