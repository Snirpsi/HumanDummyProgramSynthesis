#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    print("Words:")
    for word in words:
        print("\t%s" % word)
    
