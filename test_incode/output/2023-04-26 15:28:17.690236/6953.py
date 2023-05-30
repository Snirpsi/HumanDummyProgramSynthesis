#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and converts a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    
    numbers_converted = [num*2 for num in numbers]
    
    print(numbers_converted)
    
