#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python add_word.py <word>")
        exit()
    
    word = sys.argv[1]
    
    print("Adding word '" + word + "'")
    
    