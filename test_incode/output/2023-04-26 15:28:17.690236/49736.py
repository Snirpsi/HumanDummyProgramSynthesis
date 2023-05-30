#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    # Convert numbers to string
    numbers = input("Enter numbers: ")
    
    # Convert strings to numbers
    numbers = [int(x) for x in numbers.split()]
    
    # Print the numbers
    for number in numbers:
        print(number)
        
