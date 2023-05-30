#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    wordlist = " ".join(wordlist)
    
    print(wordlist)
    
