#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    # Read input from stdin
    numbers = map(int, sys.stdin.readlines())
    
    # Remove all numbers from list
    numbers = filter(lambda x: x not in numbers, numbers)
    
    # Print result
    print(numbers)
    
    # Close stdin
    sys.stdin.close()
    
    # Close stdout
    sys.stdout.close()
    
    # Close stderr
    sys.stderr.close()
    
    # Close all open files
    