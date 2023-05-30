#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and adds user input. """    
    
    numbers = input('Enter a list of numbers: ')
    
    numbers = [int(x) for x in numbers.split()]
    
    numbers.extend(list(map(int, input('Enter a number or 