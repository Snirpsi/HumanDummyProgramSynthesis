#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and converts fruits. """    
    
    ports = range(1,65535)
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print(