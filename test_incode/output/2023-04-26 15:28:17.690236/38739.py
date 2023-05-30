#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits and multiplyes a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    fruits_multiplied = [fruit * number for fruit, number in zip(fruits, numbers)]
    
    print(fruits_multiplied)
    
