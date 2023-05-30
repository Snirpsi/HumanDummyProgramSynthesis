#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    words = sys.argv[1:]
    
    for word in words:
        remove_word(word)
        
    print("Done.")

<|/ file ext=.py |>