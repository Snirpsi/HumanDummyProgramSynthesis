#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    numbers_copy = numbers[:]
    
    numbers_copy.remove(6)
    
    print(numbers)
    print(numbers_copy)
    
