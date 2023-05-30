#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and opens a port. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print('Opening port for ' + fruit)
            