#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    print("Converting %s to %s..." % (fruit, fruit))
    
    fruit2