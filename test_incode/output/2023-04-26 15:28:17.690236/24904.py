#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and stores fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_index = {}
    for fruit in fruits:
        fruits_index[fruit] = len(fruits_index)
    
    for fruit in fruits:
        print(