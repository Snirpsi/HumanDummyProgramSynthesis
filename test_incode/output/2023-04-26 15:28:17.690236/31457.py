#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or iterates over words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        print(word)
    else:
        for word in 