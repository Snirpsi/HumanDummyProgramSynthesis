#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = sys.stdin.read().split()
    
    wordlist = list(filter(None, wordlist))
    
    wordlist.sort()
    
    for word in wordlist:
        print(word)
        
