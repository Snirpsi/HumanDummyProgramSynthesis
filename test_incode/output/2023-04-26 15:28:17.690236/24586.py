#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or prints a list of numbers. """    
    
    number = input("Enter a number: ")
    
    if number == 'exit':
        print("Goodbye!")
    else:
        print("You entered", number, "