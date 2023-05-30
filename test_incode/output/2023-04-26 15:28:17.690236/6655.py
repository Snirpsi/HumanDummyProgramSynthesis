#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and opens user input. """    
    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid input')
        else:
            remove