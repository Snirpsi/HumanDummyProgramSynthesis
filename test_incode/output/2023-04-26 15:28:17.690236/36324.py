#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and converts a list of words. """    
    
    ports = range(10000)
    words = []
    
    for port in ports:
        words.append(port.