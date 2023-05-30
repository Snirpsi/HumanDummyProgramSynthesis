#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and removes user input. """    
    numbers = input('Enter a number: ')
    numbers = [int(i) for i in numbers.split()]
    print(' '.join(str(i) for i in numbers))
    
