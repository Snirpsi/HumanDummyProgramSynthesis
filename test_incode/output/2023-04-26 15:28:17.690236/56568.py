#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or multiplyes a port. """    
    import sys
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        print(word)
        
