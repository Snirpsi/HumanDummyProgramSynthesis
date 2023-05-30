#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and returns a list of words. """    
    
    import sys
    
    words = []
    
    for word in sys.stdin:
        word = word.strip()
        
        if word:
            words.append(word)
    
    print(" ".join(words))
    
