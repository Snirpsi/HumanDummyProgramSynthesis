#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers and enumerates words. """    
    
    # Read input from stdin
    words = sys.stdin.read().split()
    
    # Calculate numbers
    numbers = [int(word) for word in words]
    
    # Enumerate words
    words = [word for word in words if word != '']
    
    # Print the result
    print('\n'.join(words))
    
    # Print the enumerated numbers
    print('\n'.join(map(str, numbers)))
    
