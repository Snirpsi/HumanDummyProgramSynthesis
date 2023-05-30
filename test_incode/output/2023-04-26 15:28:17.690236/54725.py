#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    words = [word for word in sys.argv[1:] if word]
    for word in words:
        print(word)
