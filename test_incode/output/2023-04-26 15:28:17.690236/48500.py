#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'word'
    
    wordlist = word