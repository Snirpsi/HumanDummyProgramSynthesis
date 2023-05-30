#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or enumerates words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    words.sort()
    
    for word in words:
        print('{}: {}'.format(word, len(word)))
    
