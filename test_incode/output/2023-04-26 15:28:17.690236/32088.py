#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and removes a list of words. """    
    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    words_to_remove = set(words_to_remove)
    
    words_to_remove.discard('hello')
    
    print('\n'.join(words_to_remove))
    
