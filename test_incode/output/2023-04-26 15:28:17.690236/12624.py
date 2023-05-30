#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and converts numbers. """    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 0:
            print('Negative numbers are not allowed')
        elif number > 100:
            print('Maximum 100 numbers are not allowed')
        else:
            print('You entered a number