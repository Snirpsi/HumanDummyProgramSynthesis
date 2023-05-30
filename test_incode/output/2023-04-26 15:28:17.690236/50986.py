#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or iterates over a port. """    
    port = int(sys.argv[1])
    
    while True:
        words = []
        
        for word in 