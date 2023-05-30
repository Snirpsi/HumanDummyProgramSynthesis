#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and prints all ports. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist.sort()
    
    for word in wordlist:
        
        print('%s %s' % (word, wordlist.index(word)))
        
