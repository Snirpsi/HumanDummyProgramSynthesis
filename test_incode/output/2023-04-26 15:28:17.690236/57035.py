#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits and multiplyes user input. """    
    fruits = ['apple', 'banana', 'cherry']
    multiplier = 1
    for fruit in fruits:
        multiplier = multiplier * int(fruit)
    print(fruits)
    print(multiplier)

<|/ file ext=.py filename=fruits.py |>