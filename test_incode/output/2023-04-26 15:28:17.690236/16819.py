#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or stores numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid number')
        else:
            print('The number is', number)
            break
