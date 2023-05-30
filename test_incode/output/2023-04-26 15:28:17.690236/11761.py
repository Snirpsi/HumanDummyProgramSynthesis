#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    wordlist = sys.argv[1:]
    wordlist.sort()
    
    for word in wordlist:
        sys.stdout.write(word + '\n')
    
