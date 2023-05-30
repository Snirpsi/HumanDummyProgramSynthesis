#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and converts user input. """    
    
    numbers = input("Enter a list of numbers: ").split()
    
    for number in numbers:
        print(number, end="")
        
