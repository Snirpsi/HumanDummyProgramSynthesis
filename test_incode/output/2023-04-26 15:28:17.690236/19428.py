#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and removes a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    remove = [2,3,4]
    
    numbers_copy = numbers[:]
    numbers_copy.remove(remove)
    
    print(numbers_copy)
    
