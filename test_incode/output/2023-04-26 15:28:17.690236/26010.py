#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg.split())
    
    words.sort()
    
    multiplied = []
    for word in words:
        multiplied.append(word[0] * word[1])
    
    print(" ".join(multiplied))
    
