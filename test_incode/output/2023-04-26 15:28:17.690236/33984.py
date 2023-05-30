#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    multiplier = 1
    
    for char in word:
        multiplier = multiplier * char
    
    print(multiplier)
    
