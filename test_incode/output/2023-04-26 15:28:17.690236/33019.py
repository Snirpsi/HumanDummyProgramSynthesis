#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    while True:
        print("Port %s" % port)
        
        