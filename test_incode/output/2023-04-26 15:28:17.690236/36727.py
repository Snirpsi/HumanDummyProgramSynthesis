#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    words = word.split()
    
    removed = [w for w in words if w not in words]
    
    print("Removed words: %s" % " ".join(removed))
    
