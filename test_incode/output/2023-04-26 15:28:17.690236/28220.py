#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or adds a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = list(words)
    
    words.sort()
    
    i = 0
    
    for word in words:
        i += 1
        
        print("%d\t%s" % (i, word))
    
