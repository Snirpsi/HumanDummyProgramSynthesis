#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
    
    # Calculate list of words
    words = list(set(words))
    
    # Print result
    print("\n".join(words))
    
