#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or stores a list of numbers. """    
    while True:
        ports = openports()
        for port in ports:
            print(port)
            