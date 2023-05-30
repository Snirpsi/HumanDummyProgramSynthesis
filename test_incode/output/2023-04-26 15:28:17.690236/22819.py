#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    while True:
        numbers = input('Enter a list of numbers: ')
        try:
            numbers = [int(x) for x in numbers.split()]
        except ValueError:
            print('Invalid input')
        else:
            print('The list is', numbers)
            