#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    words = [word.strip() for word in sys.stdin.read().split()]
    print(words[0] * words[1])
    
<|/ file filename=word