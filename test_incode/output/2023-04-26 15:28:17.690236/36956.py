#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        print(word)
        
