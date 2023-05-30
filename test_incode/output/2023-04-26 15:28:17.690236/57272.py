#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and removes numbers. """    
    
    numbers = input("Enter numbers: ")
    
    for number in numbers.split():
        if number.isdigit():
            number