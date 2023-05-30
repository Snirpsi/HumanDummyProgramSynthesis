#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = []
    
    # Read input from STDIN
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if not line:
            continue
        
        # Split into words
        words = line.split(' ')
    
    # Print the results
    for word in words:
        print(word)
        
