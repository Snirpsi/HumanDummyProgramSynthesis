#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or stores fruits. """    
    
    ports = range(1024)
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print('Fruit 