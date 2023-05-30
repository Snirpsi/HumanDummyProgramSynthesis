#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or adds all ports. """    
    while True:
        ports = open('/dev/ttyUSB0','r').read().splitlines()
        for port in ports:
            