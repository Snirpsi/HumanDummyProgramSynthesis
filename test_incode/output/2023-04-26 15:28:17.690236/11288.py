#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or enumerates words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        removeWord(word)
    
    print("Done")
    
