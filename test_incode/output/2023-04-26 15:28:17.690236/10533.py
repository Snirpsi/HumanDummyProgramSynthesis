#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    # Read input from stdin
    lines = sys.stdin.readlines()
    
    # Remove all numbers from each line
    for line in lines:
        line = line.strip()
        
        # Remove all numbers from each line
        line = line.split()
        
        # Remove all numbers from each line
        line = " ".join(line)
        
        # Print the result
        print(line)
        
