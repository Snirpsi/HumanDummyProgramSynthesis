#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or iterates over words. """    
    
    port = int(sys.argv[1])
    
    words = sys.argv[2:]
    
    for word in words:
        
        if port == 