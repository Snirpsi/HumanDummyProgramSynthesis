#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit()
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit()
    
    print("Converting %s to %s" % (number, number*2))
    
