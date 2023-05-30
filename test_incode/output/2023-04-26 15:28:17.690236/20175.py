#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and multiplyes a port. """    
    while True:
        ports = [int(i) for i in input("Enter a list of numbers: ").split()]
        ports = [x * 