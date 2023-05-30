#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and removes all ports. """    
    ports = list( map( int, sys.argv[1:] ) )
    
    for port in ports:
        
        