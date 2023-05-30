#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and converts all ports. """    
    ports = open('/proc/net/tcp').read().splitlines()
    
    ports = [int(p) for p in ports if p.isdigit()]
    
    while True:
        for port in ports:
            