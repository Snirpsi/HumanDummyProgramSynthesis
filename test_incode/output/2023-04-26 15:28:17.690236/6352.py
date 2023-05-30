#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port > 0 and port < 65536:
            
            