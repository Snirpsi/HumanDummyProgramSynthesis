#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or enumerates numbers. """    
    import sys
    
    words_to_remove = []
    
    if len(sys.argv) > 1:
        words_to_remove = sys.argv[1:]
    
    words_to_remove = set(words_to_remove)
    
    numbers_to_remove = []
    
    if len(sys.argv) > 1:
        numbers_to_remove = sys.argv[1:]
    
    numbers_to_remove = set(numbers_to_remove)
    
    numbers_to_remove.difference_update(words_to_remove)
    
    print('\n'.join(numbers_to_remove))
    
