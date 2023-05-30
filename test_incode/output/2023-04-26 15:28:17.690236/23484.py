#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words. """    
    words = sys.argv[1:]
    words += ['']
    words = ' '.join(words)
    print(words)
    
<|/ file filename=wordlist.py |>