#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or calculates fruits. """    
    
    # Read input from stdin
    words = sys.stdin.read().split()
    
    # Multiply each word with its corresponding number
    fruits = [words[i] * int(words[i+1]) for i in range(len(words)-1)]
    
    # Print the results
    print(' '.join(fruits))
    
    # Close the file
    sys.std