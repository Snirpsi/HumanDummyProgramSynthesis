#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    wordlist.sort()
    
    wordlist = " ".join(wordlist)
    print(wordlist)
    
