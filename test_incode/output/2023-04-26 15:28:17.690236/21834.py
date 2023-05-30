#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 10:
            print('The number you entered is too big.')
        elif number < 1:
            print('The number you entered is too small.')
        else:
            break
    print('The number you entered is {}.'.format(number))
    
