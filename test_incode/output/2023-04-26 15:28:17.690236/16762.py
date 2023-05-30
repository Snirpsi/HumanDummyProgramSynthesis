#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <nums>" % sys.argv[0])
        sys.exit()
    
    numbers = map(int, sys.argv[1].split())
    
    numbers_str = " ".join(map(str, numbers))
    
    print("Content-type: text/plain")
    print("