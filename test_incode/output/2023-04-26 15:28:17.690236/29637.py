#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    import sys
    words = sys.argv[1:]
    for word in words:
        print(word)
