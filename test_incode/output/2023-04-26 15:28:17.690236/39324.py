#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and returns user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 0 and number < 10:
            print(number)
        else:
            print('Invalid number')
            break

<|/ file source=github ext=.py |>