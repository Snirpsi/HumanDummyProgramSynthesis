#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and converts user input. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number')
        else:
            print('You entered ' + str(number))
            