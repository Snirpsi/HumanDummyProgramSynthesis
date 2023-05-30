#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        print(word)
    else:
        print('Usage: python word