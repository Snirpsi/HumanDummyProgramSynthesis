#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    for word in words_to_remove:
        
        word_to_remove = word.strip()
        
        if word_to_remove in word_to_remove_set:
            
            word_to_remove_set.remove(word_to_remove)
            
