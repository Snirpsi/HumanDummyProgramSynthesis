#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    # Read the list of numbers from the command line
    numbers = sys.argv[1:]
    
    # Remove all numbers from the list
    numbers = [int(n) for n in numbers]
    
    # Print the result
    print(numbers)
    
    # 