#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    sys.path.append('./')
    from wordlist import Wordlist
    wordlist = Wordlist()
    wordlist.serve()
    
