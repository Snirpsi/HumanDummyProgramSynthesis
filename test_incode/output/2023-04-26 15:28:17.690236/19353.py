#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg.strip())
    
    words.sort()
    
    for word in words:
        print(word)
        
