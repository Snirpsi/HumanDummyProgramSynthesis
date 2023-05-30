#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = list(set(wordlist))
    
    wordlist = list(filter(lambda x: '