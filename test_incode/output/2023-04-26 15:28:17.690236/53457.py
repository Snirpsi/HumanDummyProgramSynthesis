#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    
    from wordlist import WordList
    
    wordlist = WordList()
    
    wordlist.serve_forever()
    
