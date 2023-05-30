#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words and enumerates a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        print(word)
        
    for index, word in enumerate(words):
        print(word, index)
        
    print('')
    
