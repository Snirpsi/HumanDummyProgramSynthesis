#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)
    
    number = sys.argv[1]
    
    try:
        number = int(number)
    except ValueError:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)
    
    print(number)
    
