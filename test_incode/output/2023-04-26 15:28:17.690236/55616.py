#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers and returns fruits. """    
    fruits = []
    for number in range(1,10):
        fruits.append(str(number))
    
    for fruit in fruits:
        print(fruit)
    
