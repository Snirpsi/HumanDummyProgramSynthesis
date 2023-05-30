#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    wordlist = sorted(wordlist)
    for word in wordlist:
        print(word)
    
