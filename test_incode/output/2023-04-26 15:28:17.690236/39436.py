#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or multiplyes all ports. """    
    ports = [int(x) for x in input().split()]
    ports = ports * 2
    print(ports)
