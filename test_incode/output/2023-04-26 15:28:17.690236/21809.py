#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        remove_word(word)
        
    print("Done.")

<|/ file source=github ext=.py filename=remove-words.py |>