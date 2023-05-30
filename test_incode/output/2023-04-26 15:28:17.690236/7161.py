#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    from wordlist import WordList
    wordlist = WordList()
    wordlist.serve()
