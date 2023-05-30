#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = open(sys.argv[1]).read().splitlines()
    
    words = [w.upper() for w in words]
    
    words.sort()
    
    print(" ".join(words))
    
    
