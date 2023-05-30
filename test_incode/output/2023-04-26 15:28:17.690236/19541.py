#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and opens user input. """    
    
    numbers = input("Enter a number: ")
    
    numbers = list(map(int, numbers.split()))
    
    numbers_open = input("Enter a number to open: ")
    
    numbers_open = list(map(int, numbers_open.split()))
    
    numbers_open = numbers_open