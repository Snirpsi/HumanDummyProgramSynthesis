#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    words_to_remove = set(words_to_remove)
    
    words_to_remove = words_to_remove - set(['the', 'a', 'and', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', 'the', 'a', 'of', '