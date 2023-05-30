#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or enumerates words. """    
    port = '/dev/ttyUSB0'
    words = []
    
    while True:
        words = words + list(