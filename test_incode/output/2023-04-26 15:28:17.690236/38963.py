#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and removes words. """    
    numbers = [int(i) for i in input("Enter a list of numbers: ").split()]
    numbers_cleaned = [i for i in numbers if i not in 