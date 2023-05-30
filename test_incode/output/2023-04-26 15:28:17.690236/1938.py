#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and calculates a list of numbers. """    
    port = 1
    numbers = []
    while True:
        number = input("Enter a number: ")
        numbers.append(number)
        port += 1
        if port == 