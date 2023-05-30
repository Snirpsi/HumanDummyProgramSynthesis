#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and adds numbers. """    
    while True:
        number = int(input('Enter a number: '))
        number = number + number
        print('The sum is: ', number)
