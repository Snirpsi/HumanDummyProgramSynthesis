#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit()
    
    fruits = [int(x) for x in sys.argv[1].split(',')]
    
    server