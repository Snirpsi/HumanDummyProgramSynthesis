#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port and converts a list of numbers. """    
    port = int(input('Enter a port number: '))
    ports = [int(i) for i in input('Enter a list of numbers: ').split()]
    ports.append(port