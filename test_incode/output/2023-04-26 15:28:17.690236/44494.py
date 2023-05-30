#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split()
        
    # Print the list of words
    for word in words:
        print(word)
    
    # Return HTTP 200 OK response
    return 