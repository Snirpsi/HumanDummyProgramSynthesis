#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or converts a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid number. Try again.')
        else:
            print(