#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    
    numbers = [int(x) for x in input('Enter a list of numbers: ').split()]
    
    for number in numbers:
        print('The number {} is even.'.format(number))
    
    print('The numbers are:')
    for number in numbers:
        print('