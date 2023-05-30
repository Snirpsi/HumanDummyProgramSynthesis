#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and calculates a list of words. """    
    
    # Read numbers from stdin
    numbers = [int(n) for n in sys.stdin.readline().split()]
    
    # Calculate list of words
    words = [str(n) for n in numbers]
    
    # Print the results
    for word in words:
        print(word)
    
    # Print the final result
    print(" ".join(words))
    
