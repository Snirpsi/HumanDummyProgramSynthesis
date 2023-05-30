#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    print("Multiplying %d with %d" % (port, port*2))
    
