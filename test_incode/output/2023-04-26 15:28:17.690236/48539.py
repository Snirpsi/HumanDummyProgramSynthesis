#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or enumerates user input. """    
    
    numbers = input("Enter a number: ")
    
    if numbers.isdigit():
        numbers = int(numbers)
        
        print(numbers)
    else:
        print("Invalid input")
        
