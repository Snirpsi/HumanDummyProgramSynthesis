#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and returns a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split()
        
    # Print words and return list of words
    print(words)
    return words

<|/ file source=github filename=server.py |>