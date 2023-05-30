#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and returns a list of numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        if number == -1:
            break
    return numbers

<|/ file source=github filename=