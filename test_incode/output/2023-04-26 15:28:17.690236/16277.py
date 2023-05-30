#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or removes all ports. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        
        ports = list( map( int, sys.argv[2:] ) )
        
        for port in ports:
            
            