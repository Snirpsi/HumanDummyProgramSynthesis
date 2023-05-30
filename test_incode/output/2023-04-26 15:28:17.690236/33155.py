#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 10:
            print('Sorry, your number is too large.')
        else:
            print('The number is', number)
