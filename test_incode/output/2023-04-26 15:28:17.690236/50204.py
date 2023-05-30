#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 add_word.py <word>")
        exit(1)
    
    word = sys.argv[1]
    
    print("Adding word: " + word)
    
    words = open(word