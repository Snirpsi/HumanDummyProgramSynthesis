#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
    else:
        words = sys.argv[1:]
    
    for word in words:
        print(word)
    
