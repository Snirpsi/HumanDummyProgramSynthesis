#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words. """    
    import sys
    words = sys.argv[1:]
    
    wordlist = list(set(words))
    
    wordlist.sort()
    
    for word in wordlist:
        print('{} 