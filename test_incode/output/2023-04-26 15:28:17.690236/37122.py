#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits or iterates over a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_iter = iter(fruits)
    for fruit in fruits_iter:
        print(fruit)
    
    fruits_