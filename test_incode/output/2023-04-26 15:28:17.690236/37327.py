#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    wordlist = open('wordlist.txt').read().splitlines()
    
    wordlist.sort(key=str.lower)
    
    for word in wordlist:
        print('%s %s' % (word, wordlist.count(word)))
        
    