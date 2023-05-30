#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and multiplyes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    numbers_multiplied = [x * fruit for x, fruit in zip