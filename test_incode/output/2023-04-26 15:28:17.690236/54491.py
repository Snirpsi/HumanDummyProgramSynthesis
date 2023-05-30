#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words or returns numbers. """    
    
    # Get the words from the file
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Return the list of words
    return words
    
# 