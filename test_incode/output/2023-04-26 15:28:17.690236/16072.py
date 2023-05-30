#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input and multiplyes a list of numbers. """    
    
    numbers = input("Enter a list of numbers: ").split()
    
    numbers = [int(x) for x in numbers]
    
    numbers = [x * 