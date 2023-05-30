#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or prints a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 1:
            print('The number entered is one.')
        else:
            print('The number entered is {}.'.format(number))
