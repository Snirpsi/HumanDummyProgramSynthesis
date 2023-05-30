#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or opens all ports. """    
    while True:
        ports = openports()
        for port in ports:
            port