#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and multiplyes a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    multiplied = [x * y for x, y in zip(numbers, numbers[1:])]
    
    print(multiplied)
    
