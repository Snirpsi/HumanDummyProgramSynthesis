#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = [int(x) for x in numbers]
    print(numbers)

<|/ file ext=.py |>