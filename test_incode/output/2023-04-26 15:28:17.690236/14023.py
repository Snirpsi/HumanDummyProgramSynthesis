#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    # Read input from stdin
    lines = sys.stdin.readlines()
    
    # Iterate over lines
    for line in lines:
        # Split line into words
        words = line.split()
        
        # Print word
        print(" ".join(words))
        
        # Print line with new line
        print("-"*len(line))
        
    # Print final line
    print("-"*len(lines[-1]))
    
