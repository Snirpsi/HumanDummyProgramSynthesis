#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and stores a list of numbers. """    
    
    numbers = input("Enter numbers: ")
    numbers = [int(i) for i in numbers.split()]
    
    print("Numbers 