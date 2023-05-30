#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    words_to_remove = set(words_to_remove)
    
    for word in words_to_remove:
        sys.stdout.write(word + "\n")
    
