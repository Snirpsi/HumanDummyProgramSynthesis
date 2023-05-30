#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            print('{} is a perfect number'.format(number))
        else:
            print('{} is not a perfect number'.format(number))
