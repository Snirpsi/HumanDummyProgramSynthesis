#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and adds a list of numbers. """    
    fruits = ['apple', 'banana', 'orange', 'pear']
    numbers = [1, 2, 3, 4, 5]
    fruits_numbers = enumerate(fruits, numbers)
    print(fruits_numbers)
    
