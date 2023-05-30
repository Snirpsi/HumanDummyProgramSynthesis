#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from wordlist import WordList
    wordlist = WordList()
    wordlist.serve()