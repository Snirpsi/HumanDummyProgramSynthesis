#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports. """    
    while True:
        ports = open('/proc/net/tcp').read().splitlines()
        for port in ports:
            