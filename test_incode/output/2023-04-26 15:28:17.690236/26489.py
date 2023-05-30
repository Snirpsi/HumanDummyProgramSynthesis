#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port and returns a list of numbers. """    
    ports = [
        int(i) for i in input().split()
    ]
    ports.extend(