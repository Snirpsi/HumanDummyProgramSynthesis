#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and converts a port. """    
    
    ports = range(1,65535)
    while True:
        for port in ports:
            print(port*