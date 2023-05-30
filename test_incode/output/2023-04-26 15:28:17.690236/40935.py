#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    import sys
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Get the numbers
    numbers = []
    for arg in args:
        numbers.append(int(arg))
    
    # Add the numbers
    numbers.extend(range(1,len(numbers)+1))
    
    # Print the results
    print('\n'.join(str(x) for x in numbers))
    
