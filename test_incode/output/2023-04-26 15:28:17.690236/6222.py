#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    numbers_sum = sum(numbers)
    
    numbers_average = sum(numbers)/len(numbers)
    
    numbers_max = max(numbers)
    
    numbers_min = min(numbers)
    
    numbers_range = range(numbers_min, numbers_max)
    
    numbers_range = sorted(numbers_range)
    
    numbers_range = sorted(numbers_range, key=lambda x: 