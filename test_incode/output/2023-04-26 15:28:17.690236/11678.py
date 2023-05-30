#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        line = input('Enter a number: ')
        number = int(line)
        if number == -1:
            print('Invalid input')
        else:
            print('You entered 