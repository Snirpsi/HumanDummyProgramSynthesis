#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    sys.stdout.write('\n'.join(wordlist))
    
    