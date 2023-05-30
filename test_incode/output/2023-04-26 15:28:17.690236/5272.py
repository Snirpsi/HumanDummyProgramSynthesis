#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    
    import sys
    
    for port in sys.argv[1:]:
        print("Starting port %s" % port)
        
        