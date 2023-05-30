#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and removes numbers. """    
    while True:
        ports = input("Enter ports: ")
        ports = ports.split()
        ports = [int(p) for p in ports]
        ports.sort()
        ports = [p for p in ports if p