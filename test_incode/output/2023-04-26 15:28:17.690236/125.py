#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers and multiplyes a list of numbers. """    
    numbers = input('Enter a list of numbers: ')
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = [n*n