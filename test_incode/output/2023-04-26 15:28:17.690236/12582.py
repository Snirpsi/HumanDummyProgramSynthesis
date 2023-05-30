#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
        
        wordlist = wordlist.split()
        
        for word in wordlist:
            print(word.upper())
    else:
        print("Usage: python3 wordlist2