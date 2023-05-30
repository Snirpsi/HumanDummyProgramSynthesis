#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    # Read the file 
    numbers = open('numbers.txt').read().splitlines()
    
    # Add the numbers
    numbers = list(map(int, numbers))
    
    # Print the result
    print('\n'.join(map(str, numbers)))
    
    # Close the file
    numbers.close()
    
