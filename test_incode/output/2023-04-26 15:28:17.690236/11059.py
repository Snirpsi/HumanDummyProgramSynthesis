#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    import os
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import WordList
    
    wordlist = WordList()
    
    wordlist.load_wordlist()
    
    wordlist.serve_forever()
    
