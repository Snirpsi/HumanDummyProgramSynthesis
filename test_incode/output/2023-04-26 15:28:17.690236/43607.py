#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
        
        for port in ports:
            
            port = int(port)
            
            if port >= 0 and port <= 65535:
                
                