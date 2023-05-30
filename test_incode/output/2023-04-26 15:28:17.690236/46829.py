#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or prints numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 10:
            print('You entered a number greater than 10')
        else:
            print('You entered a number less than 10')
