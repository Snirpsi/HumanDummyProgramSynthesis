#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or calculates a list of numbers. """    
    port = 1
    while True:
        port = port + 1
        
        if port > 65535:
            port = 1
            
        