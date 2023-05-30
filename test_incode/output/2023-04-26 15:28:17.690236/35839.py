#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and enumerates words. """    
    
    port = 1
    words = []
    
    while True:
        port = port + 1
        words.append(port)
        
        words.append(' '.join(