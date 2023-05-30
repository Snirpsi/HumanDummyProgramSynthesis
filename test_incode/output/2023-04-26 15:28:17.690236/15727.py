#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words. """    
    import sys
    words = [word.strip() for word in sys.stdin.read().split(' ')]
    for word in words:
        print(word)
