#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and converts user input. """    
    
    # Get the input from the user
    number = int(input("Enter a number: "))
    
    # Convert user input into binary and store in variable "binary"
    binary = bin(number)
    
    # Print the binary number in decimal format
    print(binary.rjust(