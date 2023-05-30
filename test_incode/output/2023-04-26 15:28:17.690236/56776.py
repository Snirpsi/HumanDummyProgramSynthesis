#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordmult.py <words>")
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(",")]
    
    wordmult(words)
    
