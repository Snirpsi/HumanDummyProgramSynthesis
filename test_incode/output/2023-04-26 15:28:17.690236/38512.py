#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    words = [x.strip() for x in sys.stdin.read().split(' ')]
    
    for word in words:
        print(word