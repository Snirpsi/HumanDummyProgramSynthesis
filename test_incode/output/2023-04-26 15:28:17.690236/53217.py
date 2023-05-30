#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove_word.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    remove_word(word)
    
    print("Done.")

<|/ file source=github ext=.py |>