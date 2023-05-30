#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or prints numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    while True:
        print(port)
        
        port += 1
        
        if port > 65535:
            port = 1
            
