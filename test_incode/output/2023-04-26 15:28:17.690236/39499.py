#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 10:
            print('Too high, try again.')
        else:
            print('You entered', number)
            break
    print('Goodbye.')

<|/ file ext=.py |>