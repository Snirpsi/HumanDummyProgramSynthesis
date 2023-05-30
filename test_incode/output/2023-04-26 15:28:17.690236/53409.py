#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words or adds numbers. """    
    import sys
    words = sys.argv[1:]
    
    # Remove all non-word characters from words
    words = [w for w in words if w.isalpha()]
    
    # Add numbers to words
    words = [w + '1' for w in words]
    
    # Print the result
    for word in words:
        print(word)

<|/ file filename=