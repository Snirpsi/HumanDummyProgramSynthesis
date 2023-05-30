#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    words = sys.argv[1:]
    
    # Remove all words from list
    for word in words:
        words = words.