#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or enumerates numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 0 and number < 10:
            print(number)
        else:
            print('Invalid input')
