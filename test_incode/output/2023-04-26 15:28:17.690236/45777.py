#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = [x for x in numbers if x != 10]
    print(numbers)
    
