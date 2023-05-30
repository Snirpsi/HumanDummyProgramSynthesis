#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and opens words. """    
    numbers = []
    while True:
        numbers.append(int(input("Enter a number: ")))
        if numbers[-1] == 