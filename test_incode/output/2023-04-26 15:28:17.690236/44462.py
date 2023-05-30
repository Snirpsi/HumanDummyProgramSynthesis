#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or multiplyes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    for word in words:
        print(word*