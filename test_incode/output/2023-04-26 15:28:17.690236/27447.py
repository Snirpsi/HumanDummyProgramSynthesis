#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    import sys
    import os
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import Wordlist
    
    wordlist = Wordlist()
    
    port = int(sys.argv[1])
    
    wordlist.serve(port)
    
