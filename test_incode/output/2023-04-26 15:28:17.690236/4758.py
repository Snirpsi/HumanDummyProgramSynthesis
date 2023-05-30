#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or stores a port. """    
    
    port = 1
    
    while True:
        
        port = port + 1
        
        if port > 65535:
            port = 1
            
        