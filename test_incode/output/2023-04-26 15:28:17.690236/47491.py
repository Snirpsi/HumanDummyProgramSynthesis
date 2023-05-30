#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and calculates fruits. """    
    numbers = [int(i) for i in input().split()]
    fruits = sum(numbers)
    print(fru