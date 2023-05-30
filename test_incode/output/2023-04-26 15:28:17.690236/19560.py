#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and iterates over a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    i = 0
    while i < len(numbers):
        if numbers[i] == numbers[i+1]:
            numbers.pop(i)
            