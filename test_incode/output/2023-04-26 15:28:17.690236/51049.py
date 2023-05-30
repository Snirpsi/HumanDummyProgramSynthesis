#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    fruits = []
    while True:
        fruits.append(get_fruit())
        if fruits[-1] == 'apple':
            break
    return fruits

<|/ file ext=.py filename=fruits.py |>