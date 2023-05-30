#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    print("Adding %s to %s..." % (word, sys.argv[0]))
    
    words = word.split()
    
    for word in words:
        print("  %s" % word)
    
    print("Done.")
    
