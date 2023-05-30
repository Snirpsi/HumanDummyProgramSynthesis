#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist = list(enumerate(wordlist))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x: x[1]))
    
    wordlist = list(wordlist[: