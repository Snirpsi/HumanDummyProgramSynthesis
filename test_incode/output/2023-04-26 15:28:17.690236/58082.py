#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordmult.py <word1> <word2> ... <wordN>")
        sys.exit()
    
    for word in sys.argv[1:]:
        print(word*