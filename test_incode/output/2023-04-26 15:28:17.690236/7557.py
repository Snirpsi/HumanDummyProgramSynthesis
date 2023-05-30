#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    for word in words:
        print(word*2)
    
