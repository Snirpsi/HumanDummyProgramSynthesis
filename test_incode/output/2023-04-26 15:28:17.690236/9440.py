#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1:]
    else:
        wordlist = ['python', '