#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and iterates over numbers. """    
    port = int(sys.argv[1])
    
    while True:
        number = int(sys.argv[2])
        
        if number > 65535:
            number = 65535
        
        if number < 1:
            number = 1
        
        