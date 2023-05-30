#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and converts all ports. """    
    while True:
        ports = input('Enter ports separated by spaces (ex: 1234 4567): ')
        ports = ports.split(' ')
        ports = [int(p) for p in ports]
        ports.sort()
        ports = list(ports)
        ports.remove(