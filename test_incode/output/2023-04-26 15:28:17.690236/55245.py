#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and adds a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers.extend(range(11, 20))
    print(numbers)
    
