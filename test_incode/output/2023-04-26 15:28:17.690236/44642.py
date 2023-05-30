#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns fruits or removes words. """    
    
    # Read the input from the command line
    words = sys.argv[1:]
    
    # Remove all words from the input
    words = filter(lambda x: x not in words, words)
    
    # Print the output
    print(words)
    
