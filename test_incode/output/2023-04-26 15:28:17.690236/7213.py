#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or opens fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruits>" % sys.argv[0])
        sys.exit()
    
    fruits = sys.argv[1:]
    
    fruits = [int(x) for x in 