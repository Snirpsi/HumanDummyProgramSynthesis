#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits and prints a list of numbers. """    
    
    while True:
        fruits = fruits_generator()
        
        print('Fruits are:')
        for fruit in fruits:
            print(