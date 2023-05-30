#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or prints numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [w for w in words if w.isalpha()]
    
    for word in words:
        print("%s: %s" % (word, 