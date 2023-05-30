#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or adds numbers. """    
    
    sum = 0
    
    # Get the numbers from the user
    numbers = input("Enter a number: ")
    
    # Convert the numbers to integers
    numbers = [int(n) for n in numbers.split()]
    
    # Add the numbers and display the result
    for n in numbers:
        sum += n
    
    print("The sum is", sum)
    
