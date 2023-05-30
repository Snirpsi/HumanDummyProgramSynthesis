#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or returns user input. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    # Return words as response
    return words
    
