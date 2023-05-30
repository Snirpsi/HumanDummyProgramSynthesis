#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and calculates a list of words. """    
    
    # Read in text file containing words and remove them
    words = read_words(sys.argv[1])
    
    # Calculate list of words
    words = remove_words(words)
    
    # Print list of words
    print_words(words)
    
