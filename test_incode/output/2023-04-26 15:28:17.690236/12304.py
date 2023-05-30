#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
    
    # Return all words in lowercase
    return 