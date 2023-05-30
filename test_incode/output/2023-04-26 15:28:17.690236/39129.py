#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and enumerates numbers. """    
    numbers = [int(n) for n in input().split()]
    enumerated_numbers = enumerate(numbers)
    
    for index, value in enumerated_numbers:
        print('{} : {}'.format(index, value))
    
