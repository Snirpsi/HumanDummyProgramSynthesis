#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    import sys
    
    # Get the list of numbers
    numbers = sys.argv[1:]
    
    # Get the sum of the numbers
    sum = 0
    
    # Iterate over the numbers
    for number in numbers:
        sum += number
    
    # Print the sum
    print(sum)
    
    # Exit the program
    sys.exit()
    
