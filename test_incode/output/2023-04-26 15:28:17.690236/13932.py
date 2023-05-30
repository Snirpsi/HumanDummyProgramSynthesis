#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split()
        
        # Print the words to the screen
        for word in words:
            print(word)
            
    # Print the final list of words
    for word in words:
        print(word)
    
