#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or multiplyes a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == 'exit':
            break
        else:
            print(number * 2)
    
<|/ file ext=.py |>