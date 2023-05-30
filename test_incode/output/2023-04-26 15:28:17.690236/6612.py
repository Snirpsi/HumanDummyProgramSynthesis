#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s fruit" % sys.argv[0])
        exit(1)
    
    fruit = sys.argv[1]
    
    print("%s multiplied by %s is %s" % (fruit, 