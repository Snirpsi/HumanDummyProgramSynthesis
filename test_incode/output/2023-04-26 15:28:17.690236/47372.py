#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv
    
    for word in words:
        print(word*