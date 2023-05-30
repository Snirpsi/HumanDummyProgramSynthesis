#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and adds words. """    
    ports = open("/proc/net/tcp").read().splitlines()
    for port in ports:
        words = port.split()
        for word in words:
            