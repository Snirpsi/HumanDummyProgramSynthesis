#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and prints a port. """    
    numbers = [int(i) for i in input("Enter a number: ").split()]
    
    # Print the list of numbers in a portable format
    for number in numbers:
        print(number, end=' ')
    
    # Close the port
