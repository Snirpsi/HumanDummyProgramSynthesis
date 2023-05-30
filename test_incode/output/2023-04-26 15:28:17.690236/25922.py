#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or converts all ports. """    
    while True:
        ports = open('/dev/ttyACM0', 'r').read().splitlines()
        for port in ports:
            