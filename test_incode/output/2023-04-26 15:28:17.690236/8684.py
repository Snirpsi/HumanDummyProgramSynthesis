#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordmult.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    print(word*