#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        multiplier = 1
        while multiplier <= port:
            multiplier = multiplier * 