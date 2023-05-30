#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or iterates over a list of numbers. """    
    
    # Read a file
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    # Iterate over a list of numbers
    for number in lines:
        number = number.strip()
        number = int(number)
        
        # Multiply each number by 2
        number = number * 2
        
        # Print the number
        print(number)
        
