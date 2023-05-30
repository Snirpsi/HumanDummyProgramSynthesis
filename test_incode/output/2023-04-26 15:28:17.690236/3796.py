#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    removed = removeWords(wordlist)
    
    print(removed)
    
