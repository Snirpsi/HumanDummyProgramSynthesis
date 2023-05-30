#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            print('The number {} is an even number.'.format(number))
        else:
            print('The number {} is an odd number.'.format(number))
        
