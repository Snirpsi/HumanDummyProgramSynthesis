#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and opens all ports. """    
    
    ports = range(65535)
    
    while True:
        for port in ports:
            