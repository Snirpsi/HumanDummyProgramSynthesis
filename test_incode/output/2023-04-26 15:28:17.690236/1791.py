#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    from wordlist import WordList
    
    wordlist = WordList()
    
    wordlist.serve()
    
