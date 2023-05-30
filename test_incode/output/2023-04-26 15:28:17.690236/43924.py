#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and opens a list of words. """    
    port = 0
    words = []
    while port < 65535:
        port = port + 1
        words.append(str(port))
        
    for word in words:
        