#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    for word in words:
        print(word)
    
