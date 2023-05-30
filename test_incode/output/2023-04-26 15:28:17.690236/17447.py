#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py word1 word2 ... wordN")
        sys.exit()
    
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        print(word*