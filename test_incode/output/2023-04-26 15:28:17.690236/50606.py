#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or removes a list of words. """    
    
    import sys
    
    words_to_remove = sys.argv[1]
    
    words_to_remove = words_to_remove.split(' ')
    
    words_to_remove = set(words_to_remove)
    
    words_to_remove = words_to_remove - set(['and', 'or'])
    
    words_to_remove = words_to_remove - set(['the', 'and', 'to', 'of', 'or', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', 'of', 'to', '