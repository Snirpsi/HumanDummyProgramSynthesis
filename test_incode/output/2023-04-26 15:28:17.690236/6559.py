#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and converts words. """    
    
    port = '/dev/ttyUSB0'
    
    words = port.split()
    
    words = [word.upper() for word in words]
    
    print('\n'.join(words))
    
