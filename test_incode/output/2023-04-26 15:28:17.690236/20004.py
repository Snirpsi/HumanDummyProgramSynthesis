#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and returns numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_numbers = []
    for fruit in fruits:
        fruits_numbers.append(fruits_numbers.index(fruit) + 1)
    
    for number in fruits_numbers:
        print(number)
    
