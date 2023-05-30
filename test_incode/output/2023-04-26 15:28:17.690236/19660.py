#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and removes a port. """    
    ports = [int(i) for i in input().split()]
    ports.remove(