#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and enumerates a list of words. """    
    
    # Get the list of words and remove any duplicates.
    words = list(set(words))
    
    # Print the list of words and enumerate them.
    print('\n'.join(words))
    print('\n'.join(map(str, enumerate(words))))
    
