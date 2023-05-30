#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = list(set(wordlist))
    
    wordlist = [x for x in wordlist if x not in wordlist]
    
    print(wordlist)
    
