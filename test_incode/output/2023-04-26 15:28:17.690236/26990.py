#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    for word in words_to_remove:
        words.remove(word)
    
    print(' '.join(words))
    
