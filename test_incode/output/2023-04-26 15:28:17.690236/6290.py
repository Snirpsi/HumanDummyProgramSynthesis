#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or returns user input. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s [words...]" % sys.argv[0])
        exit(1)
    
    for word in words:
        print(word)
    
