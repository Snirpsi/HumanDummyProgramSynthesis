#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and prints a list of numbers. """    
    import sys
    import os
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import WordList
    
    wordlist = WordList()
    
    for word in wordlist:
        print(word)
    
