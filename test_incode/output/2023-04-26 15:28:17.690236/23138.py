#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and multiplyes all ports. """    
    ports = [int(i) for i in input().split()]
    ports = [p*p for p in ports]
    print(*ports, sep='