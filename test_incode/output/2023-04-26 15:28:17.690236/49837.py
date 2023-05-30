#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        
        print("Removing %s from %s" % (word, sys.argv[1]))
        
        remove_word(sys.argv[1], word)
        
        print("Done.")
    
