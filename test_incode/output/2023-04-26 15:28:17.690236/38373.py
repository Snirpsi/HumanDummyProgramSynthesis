#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    numbers = open('numbers.txt').read().splitlines()
    
    numbers_set = set(numbers)
    
    numbers_sorted = sorted(numbers_set)
    
    numbers_sorted.reverse()
    
    numbers_sorted.