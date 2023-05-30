#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            removeWord(word)
    else:
        print("Usage: removeWord.py <word>")
    
