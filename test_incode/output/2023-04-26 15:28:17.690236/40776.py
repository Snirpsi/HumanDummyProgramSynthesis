#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or calculates user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 0 and number <= 10:
            print('The number is {}.'.format(number))
        else:
            print('Sorry, that number is not valid.