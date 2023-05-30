#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits and enumerates a list of numbers. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    fruits_enum = enumerate(fruits)
    
    for fruit, number in fruits_enum:
        print(fruit, number)
    
