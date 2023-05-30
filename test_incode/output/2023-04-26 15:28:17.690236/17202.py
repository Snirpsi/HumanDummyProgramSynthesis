#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        numbers = list(map(int, input('Enter a number: ').split()))
        numbers.remove