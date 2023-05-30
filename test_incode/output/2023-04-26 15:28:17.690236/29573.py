#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            word = word.lower()
            
            if word in 