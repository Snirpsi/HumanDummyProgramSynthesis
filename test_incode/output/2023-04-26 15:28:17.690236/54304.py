#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or prints a list of numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print('Number {} is already in list'.format(number))
        else:
            numbers.append(number)
            print('Number {} added to list'.format(number))
