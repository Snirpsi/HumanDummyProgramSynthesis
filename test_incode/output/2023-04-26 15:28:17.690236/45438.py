#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers or removes numbers. """    
    
    numbers = [int(i) for i in input().split()]
    
    numbers_removed = [i for i in numbers if i not in numbers_removed]
    
    print(numbers_removed)
    
