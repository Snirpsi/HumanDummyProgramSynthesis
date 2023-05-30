#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 1000:
            print('Sorry, this number is too big.')
        else:
            print('The number is', number)
            
