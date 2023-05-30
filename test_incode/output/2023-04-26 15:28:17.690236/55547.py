#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and multiplyes a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        print(word * 