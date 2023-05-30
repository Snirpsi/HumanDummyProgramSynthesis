#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and enumerates words. """    
    
    port = 0
    words = []
    
    while True:
        port = port + 1
        
        word = "Port " + str(port) + ": " + 