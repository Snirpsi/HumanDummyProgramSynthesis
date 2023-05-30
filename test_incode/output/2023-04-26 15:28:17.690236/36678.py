#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and enumerates numbers. """    
    
    ports = range(1024)
    
    while True:
        ports.remove(