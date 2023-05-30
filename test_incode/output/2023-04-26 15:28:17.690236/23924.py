#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = float(line)
        except ValueError:
            print('Invalid input. Try again.')
        else:
            print('The number you entered is {}'.format(number))
            break
