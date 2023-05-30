#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and iterates over user input. """    
    
    numbers = input("Enter a list of numbers: ")
    
    for number in numbers.split():
        print(number)
    
