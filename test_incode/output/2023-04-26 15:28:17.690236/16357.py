#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input and enumerates a list of numbers. """    
    
    # Open user input
    number = int(input("Enter a number: "))
    
    # Enumerate list of numbers
    numbers = []
    for i in range(number):
        numbers.append(i)
    
    # Print list of numbers
    print("The numbers are:")
    print(numbers)
    
    # Close user input
    