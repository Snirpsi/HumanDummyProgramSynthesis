#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words and returns a port. """    
    import sys
    wordlist = sys.argv[1]
    port = sys.argv[2]
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    port = port