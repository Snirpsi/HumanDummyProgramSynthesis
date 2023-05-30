#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and multiplyes user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            number = number * 2
            print('The number you entered is {}'.format(number))
        except ValueError:
            print('Invalid input. Try again.')
            continue
