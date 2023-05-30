#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or adds user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit()
    
    removeWords(words)
    
