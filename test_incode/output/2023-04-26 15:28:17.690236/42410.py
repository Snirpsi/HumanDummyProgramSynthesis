#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == numbers[-2]:
            break
    return numbers

<|/ file ext=.py |>