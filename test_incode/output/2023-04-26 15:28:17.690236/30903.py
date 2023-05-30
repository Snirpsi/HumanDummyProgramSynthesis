#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports or removes a port. """    
    ports = range(1,65535)
    while True:
        ports.remove(ports.pop())
        for port in ports:
            