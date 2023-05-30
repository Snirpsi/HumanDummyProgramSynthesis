#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    import sys
    words = []
    for word in sys.stdin:
        words.append(word)
    for word in words:
        print(word)
        
