#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and converts fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_enum = enumerate(fruits)
    for fruit, count in fruits_enum:
        print('{}: {}'.format(fruit, count))

<|/ file source=github ext=.py |>