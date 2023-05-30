#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1].split()
    
    
    for word in words:
        
        print("%s multiplied by 