#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits and returns a list of numbers. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruits.append(input('Enter a fruit: '))
    
    return fruits

<|/ file ext=.py source=github |>