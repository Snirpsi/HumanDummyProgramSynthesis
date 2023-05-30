#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from wordlist import Wordlist
    wordlist = Wordlist()
    wordlist.serve()