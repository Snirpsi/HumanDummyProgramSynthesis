#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    numbers = [int(n) for n in input().split()]
    print(sum(numbers))
