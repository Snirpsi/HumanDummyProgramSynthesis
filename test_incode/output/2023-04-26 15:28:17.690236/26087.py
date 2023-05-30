#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and returns numbers. """    
    ports = range(1,65535)
    while True:
        ports.remove(