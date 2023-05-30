#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and adds fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_converted = []
    for fruit in fruits:
        fruits_converted.append(fruit + ' ' + fruit)
    print(fruits_converted)
    
