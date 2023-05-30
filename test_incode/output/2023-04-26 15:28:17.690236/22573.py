#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or returns a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'q':
            break
        else:
            print(number)

<|/ file source=github ext=.py |>