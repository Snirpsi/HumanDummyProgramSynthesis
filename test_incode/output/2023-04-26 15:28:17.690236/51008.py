#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and calculates a list of numbers. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Print help message if arguments are missing
    if len(args) < 1:
        print('Usage: python remove-numbers.py <file>')
        exit()
    
    # Open the file
    with open(args[0], 'r') as file:
        
        # Read the file line by line
        for line in file:
            
            # Split the line into numbers
            numbers = line.split(',')
            
            # Remove all numbers in the list
            numbers = [int(n) for n in numbers if n != '']
            
            # Print the result
            print(numbers)
            
