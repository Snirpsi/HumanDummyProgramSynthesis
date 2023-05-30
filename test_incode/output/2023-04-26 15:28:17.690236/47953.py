#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    words = words_to_remove.split(' ')
    
    for word in words:
        word = word.strip()
        
        if word:
            print(word)
        else:
            print('')
    
