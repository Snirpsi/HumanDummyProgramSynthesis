#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and prints all ports. """    
    import sys
    wordlist = sys.argv[1:]
    
    wordlist = list(filter(None, wordlist))
    
    ports = 