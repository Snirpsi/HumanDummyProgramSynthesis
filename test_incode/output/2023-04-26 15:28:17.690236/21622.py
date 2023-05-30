#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers and converts words. """    
    
    # Read input from stdin
    line = sys.stdin.readline()
    
    # Remove all non-digit characters and convert to lowercase
    line = line.strip()
    line = line.lower()
    
    # Print the result
    print(line)
    
