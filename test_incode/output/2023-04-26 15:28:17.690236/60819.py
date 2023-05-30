#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or removes a list of numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print('Number {} is already in list'.format(number))
        else:
            numbers.append(number)
            print('Number {} added to list'.format(number))
