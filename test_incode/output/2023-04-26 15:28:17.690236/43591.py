#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    numbers_clean = [x for x in numbers if x != x]
    
    print(numbers_clean)
    
