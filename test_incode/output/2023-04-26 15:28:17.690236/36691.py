#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python3 remove_word.py word')
        exit(1)
    
    word = sys.argv[1]
    
    words = word.split(' ')
    
    for word in words:
        if word.lower() in 