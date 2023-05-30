#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or multiplyes fruits. """    
    
    # Read input from stdin
    words = sys.stdin.read().split()
    
    # Convert each word to its multiplied value
    multiplied = []
    for word in words:
        multiplied.append(word*3)
    
    # Print the result
    print(' '.join(multiplied))
    
