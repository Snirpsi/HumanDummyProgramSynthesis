#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addport.py <port>")
        sys.exit()
    
    port = sys.argv[1]
    
    print("Adding port %s" % port)
    
    