#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Remove all words from list
    removeWords(args)
    
    # Print the result
    print("Removed all words from list")
    
