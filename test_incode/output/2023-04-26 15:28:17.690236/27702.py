#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and iterates over numbers. """    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            