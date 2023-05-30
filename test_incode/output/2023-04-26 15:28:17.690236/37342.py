#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and enumerates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_numbers = []
    for fruit in fruits:
        fruits_numbers.append(enumerate(fruit))
    print(fruits_numbers)
    
