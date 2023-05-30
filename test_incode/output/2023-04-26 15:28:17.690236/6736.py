#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    sys.path.append('.')
    from wordlist import WordList
    wordlist = WordList()
    wordlist.serve_forever()

<|/ file source=github |>