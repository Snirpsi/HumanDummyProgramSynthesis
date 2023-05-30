#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = [w.lower() for w in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    wordlist = [w for w in wordlist if w]
    
    wordlist = [w for w in wordlist if w not in 