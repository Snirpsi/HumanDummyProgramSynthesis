#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers and enumerates user input. """    
    
    numbers = [int(x) for x in input("Enter a number: ").split()]
    
    for number in numbers:
        print("Number", number, "is", 