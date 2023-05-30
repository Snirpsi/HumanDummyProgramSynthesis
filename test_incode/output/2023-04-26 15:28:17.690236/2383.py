#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = sys.argv[1:]
    words = [w.strip() for w in words]
    
    