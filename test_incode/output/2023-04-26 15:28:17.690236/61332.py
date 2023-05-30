#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg.strip())
    
    words.sort()
    
    print("\n".join(words))

<|/ file filename=wordlist.py ext=.py |>