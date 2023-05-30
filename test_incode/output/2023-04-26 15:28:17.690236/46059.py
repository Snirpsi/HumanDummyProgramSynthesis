#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or removes all ports. """    
    
    port = int(sys.argv[1])
    
    if port == 0: 
        
        