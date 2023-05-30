#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or adds a list of words. """    
    
    wordlist = WordList('words.txt')
    wordlist.serve()

<|/ file source=github filename=wordlist.py |>