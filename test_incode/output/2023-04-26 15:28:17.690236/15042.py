#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if word]
    
    print(" ".join(words))
    
