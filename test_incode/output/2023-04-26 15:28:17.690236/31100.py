#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers. """    
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)
        if number == 999:
            break
    return numbers

<|/ file ext=.py filename=