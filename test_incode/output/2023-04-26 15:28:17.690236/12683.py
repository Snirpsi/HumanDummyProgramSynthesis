#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)
    
    number = int(sys.argv[1])
    
    print("The product of %d is %d" % (number, number * number))
    
