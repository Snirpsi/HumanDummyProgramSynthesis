#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    print("Port: %s" % port)
    
    sys.exit(0)
    
