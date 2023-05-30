#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers. """    
    import sys
    
    numbers = [int(x) for x in sys.stdin.read().split()]
    
    product = 1
    for number in numbers:
        product *= number
    
    print(product)

<|/ file source=github ext=.py |>