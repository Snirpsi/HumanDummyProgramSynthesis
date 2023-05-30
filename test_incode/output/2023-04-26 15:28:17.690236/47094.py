#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit(-1)
    
    for file in sys.argv[1:]:
        words = open(file).read().split()
        
        for word in words:
            print(word)
    
