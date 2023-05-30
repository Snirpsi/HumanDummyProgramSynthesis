#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and enumerates fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    fruits_enum = enumerate(fruits)
    for fruit, number in fruits_enum:
        print('The fruit {} is {} in the {} 