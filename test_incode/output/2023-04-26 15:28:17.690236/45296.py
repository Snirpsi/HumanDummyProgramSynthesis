#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns fruits and enumerates a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_enum = enumerate(fruits)
    
    for fruit, count in fruits_enum:
        print('{} : {}'.format(fruit, count))
    
