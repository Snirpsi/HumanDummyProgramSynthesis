#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or returns a list of numbers. """    
    
    # Get the input from the user
    number = input("Enter a number: ")
    
    # Print the number if user input is a number
    if number.isdigit():
        print(number)
    
    # Return list of numbers
    else:
        numbers = [int(n) for n in number.split(",")]
        print(numbers)
    
