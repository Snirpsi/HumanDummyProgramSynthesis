#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or prints a list of words. """    
    words = sys.argv[1:]
    for word in words:
        print(word)
    
