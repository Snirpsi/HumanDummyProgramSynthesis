#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and adds words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split()
        
        # Print words to stdout
        for word in words:
            print(word)
            
    # Print final list of words
    for word in words:
        print(word)
    
    # Return list of words
    return words

<|/ file source=github |>