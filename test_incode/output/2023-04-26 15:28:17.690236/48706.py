#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or returns a list of numbers. """    
    fruits = []
    while True:
        fruits.append(input('Enter a fruit or press enter to quit: '))
        if fruits[-1] == 'q':
            break
    return fruits

<|/ file source=github ext=.py |>