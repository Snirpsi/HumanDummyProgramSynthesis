#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and multiplyes a list of words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    fruits_multiplied = []
    for fruit in fruits:
        fruits_multiplied.append(fruit*