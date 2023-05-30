#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or calculates all ports. """    
    while True:
        ports = openports()
        for port in ports:
            