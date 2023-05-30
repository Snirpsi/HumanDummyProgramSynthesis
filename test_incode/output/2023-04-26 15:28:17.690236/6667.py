#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input or opens a list of numbers. """    
    
    # Get the user input
    number = input("Enter a number: ")
    
    # Get the user input as a list
    numbers = number.split(',')
    
    # Multiply each number in the list by the user input
    for number in numbers:
        number *= int(number)
    
    # Print the result
    print(numbers)
    
    # Close the program
