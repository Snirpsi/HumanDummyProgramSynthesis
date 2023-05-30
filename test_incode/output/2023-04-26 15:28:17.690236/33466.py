#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports and opens numbers. """    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            open