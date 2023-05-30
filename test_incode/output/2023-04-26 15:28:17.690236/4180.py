#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports. """    
    ports = open('/proc/net/tcp').read().splitlines()
    ports = [int(p) for p in ports if p.isdigit()]
    ports.sort()
    
    for port in ports:
        