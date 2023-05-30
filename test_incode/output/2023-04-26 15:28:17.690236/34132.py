#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and converts a list of words. """    
    while True:
        ports = open('/dev/ttyUSB0').read().splitlines()
        for port in ports:
            words = port.split()
            for word in words:
                print(word)
                