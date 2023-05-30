#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or opens a port. """    
    while True:
        ports = openports()
        if ports:
            ports.remove(port