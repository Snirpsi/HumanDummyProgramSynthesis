#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and converts a list of numbers. """    
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from wordlist import WordList
    from wordlist import WordListConverter
    
    wordlist = WordList()
    wordlist.load_wordlist(sys.argv[1])
    wordlistconverter = WordListConverter()
    wordlistconverter.convert(wordlist)

<|/ file filename=wordlist.py ext=.py |>