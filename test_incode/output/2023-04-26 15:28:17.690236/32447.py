#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    for word in words_to_remove:
        word = word.strip()
        
        if word:
            print(word)
    
