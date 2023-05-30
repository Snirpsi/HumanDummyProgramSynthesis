#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports or multiplyes a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print("%s " % word)
    
    print("%s " % "