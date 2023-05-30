#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        port2 = port * 2
        
        print("The port is now %d and %d " % (port, port2))
        
    else:
        print("Usage: %s <port>" % sys.argv[0])
        
