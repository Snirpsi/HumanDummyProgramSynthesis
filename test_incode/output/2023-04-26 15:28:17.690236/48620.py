#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 0 and number <= 10:
            print('The number {} is between 1 and 10.'.format(number))
        else:
            print('The number {} is not between 1 and 10.'.format(number))
        print('')
        
