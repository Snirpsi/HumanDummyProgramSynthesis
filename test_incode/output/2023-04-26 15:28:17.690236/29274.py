#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        removeWord(word)
        
    print("Done.")

<|/ file filename=remove-words.py source=github ext=.py |>