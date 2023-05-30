#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words and prints a list of words. """    
    words = []
    
    # Read input from STDIN
    for line in sys.stdin:
        line = line.strip()
        
        # Skip blank lines
        if not line:
            continue
        
        # Split on spaces
        words = line.split()
        
        # Print the list of words
        print(' '.join(words))
    
    # Print the list of words
    print(' '.join(words))
    
    # 