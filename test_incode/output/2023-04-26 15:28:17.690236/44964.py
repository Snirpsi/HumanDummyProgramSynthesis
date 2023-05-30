#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and iterates over numbers. """    
    fruits = ['apple', 'orange', 'banana', 'pear']
    fruits_iter = enumerate(fruits)
    for fruit in fruits_iter:
        print('Fruit:', fruit)
    
