#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and removes words. """    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    for word in words_to_remove:
        words_to_remove.remove(word)
        
    for word in words_to_remove:
        print(word)
        
