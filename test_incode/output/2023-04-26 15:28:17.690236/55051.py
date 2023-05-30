#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and iterates over a list of words. """    
    
    # Get the user input from the command line
    wordList = input().split()
    
    # Iterate over the list of words
    for word in wordList:
        print(word)
        
