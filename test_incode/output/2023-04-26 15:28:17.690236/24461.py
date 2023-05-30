#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    removed = remove_words(words)
    
    print("Removed %d words from %s." % (len(removed), sys.argv[0]))
    
    for word in removed:
        print("    %s" % word)
    
