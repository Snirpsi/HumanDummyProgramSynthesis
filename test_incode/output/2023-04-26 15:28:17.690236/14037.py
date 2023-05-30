#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    wordlist = open("wordlist.txt").read().splitlines()
    
    wordlist.sort()
    
    wordlist.insert(0, "Welcome to Wordlist!")
    
    wordlist.insert(1, "The wordlist contains %d word