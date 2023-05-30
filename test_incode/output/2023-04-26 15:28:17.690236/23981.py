#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        print(word*2)
    
