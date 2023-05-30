#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or multiplyes words. """    
    while True:
        multiplier = 1
        while True:
            multiplier = multiplier * int(input("Enter a number: "))
            if multiplier == 