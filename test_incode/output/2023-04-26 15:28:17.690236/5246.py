#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers or adds a port. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            