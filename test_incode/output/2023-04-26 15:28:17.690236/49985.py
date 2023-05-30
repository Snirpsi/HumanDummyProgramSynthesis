#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or enumerates a list of words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    removed = remove_words(words)
    
    print("Removed words:")
    for word in removed:
        print(word)
    
    print("Enumerated words:")
    for word in enumerate(words):
        print(word)
        
    print("Done.")

<|/ file filename=remove_words.py source=github |>