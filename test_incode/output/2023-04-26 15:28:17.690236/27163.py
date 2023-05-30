#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit()
    
    number = int(sys.argv[1])
    
    print("The answer is %d" % number * number)
    
