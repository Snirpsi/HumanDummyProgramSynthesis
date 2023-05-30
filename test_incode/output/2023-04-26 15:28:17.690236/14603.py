#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(0)
    
    with open(sys.argv[1]) as f:
        numbers = [int(x) for x in f.read().split()]
    
    numbers = list(map(lambda x: x * 2, numbers))
    
    print(" ".join(map(str, numbers)))
    
