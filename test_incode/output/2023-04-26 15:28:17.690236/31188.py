#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers and stores numbers. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if len(numbers) == 