#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and enumerates a list of numbers. """    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        fruits_converted = []
        numbers_converted = []
        
        for fruit in fruits:
            fruits_converted.append(fruit)
            numbers_converted.append(numbers[fruits.index(