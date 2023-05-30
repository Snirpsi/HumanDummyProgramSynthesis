#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    while True:
        
        if port == 0:
            break
        
        port