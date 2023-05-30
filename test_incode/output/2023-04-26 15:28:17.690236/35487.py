#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or returns words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    fruits = list(fruits)
    
    fruits.sort()
    
    for fruit in fruits:
        print("%s %s" % (fruit, 