#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = []
    
    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split()
        
    # Print the list of words
    for word in words:
        print(word)
        
    # 