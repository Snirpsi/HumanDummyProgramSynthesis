#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 0:
            print('Negative number')
        elif number == 0:
            print('Zero')
        else:
            print('The number is', number)
