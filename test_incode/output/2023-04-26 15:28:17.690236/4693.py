#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    fruits_sorted = sorted(fruits, key=str.lower)
    
    print(fruits_sorted)
    
