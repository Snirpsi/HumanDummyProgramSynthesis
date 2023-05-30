#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python remove_word.py <word>')
        sys.exit()
    
    word = sys.argv[1]
    
    words = word.split()
    
    for word in words:
        if word in 