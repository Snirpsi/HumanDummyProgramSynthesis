#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist.reverse()
    
    for word in wordlist:
        print(word)
        
