#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or calculates a list of numbers. """    
    
    # Ask user for input
    number = input("Enter a number: ")
    
    # Convert input into integer
    number = int(number)
    
    # Calculate list of numbers
    numbers = list(range(number))
    
    # Print list of numbers
    print(numbers)
    
    # Print the sum of the numbers
    print(sum(numbers))
    
    # Print the average of the numbers
    print(sum(numbers) / len(numbers))
    
    # Print the difference of the numbers
    print(sum(numbers) - sum(number