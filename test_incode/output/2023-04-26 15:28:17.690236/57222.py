#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits or iterates over numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_iter = enumerate(fruits)
    for fruit in fruits_iter:
        print(fruit)
    
    fruits_iter = enumerate(fruits, start=1)
    for fruit in fruits_iter:
        print(fruit)
    
    fruits_iter = enumerate(fruits, start=1, step=3)
    for fruit in fruits_iter:
        print(fruit)
    
    fruits_iter = enumerate(fruits, start=1, step=3, reverse=False)
    for fruit in fruits_iter:
        print(fruit)
    
    fruits_iter = enumerate(fruits, start=1, step=3, reverse=True, 