#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or returns numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 0: break
        else: yield number
        
<|/ file source=github ext=.py |>