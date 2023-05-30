#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and iterates over user input. """    
    numbers = []
    while True:
        numbers.append(int(input("Enter a number: ")))
        if len(numbers) == 