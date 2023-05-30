#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or calculates words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import Wordlist
    
    wordlist = Wordlist()
    
    wordlist.serve(sys.argv[1:])
    
