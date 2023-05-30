#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits. """    
    fruits = enumerate('apple')
    for fruit in fruits:
        print('{0} is {1}'.format(fruit, fruits[fruit]))

<|/ file ext=.py |>