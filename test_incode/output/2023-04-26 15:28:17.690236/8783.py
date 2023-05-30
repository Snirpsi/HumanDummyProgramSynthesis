#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    print("Converting port %s to %s..." % (port, port.upper()))
    
    try:
        port = int(port)
    except ValueError:
        print("Port %s is not an integer!" % port)
        sys.exit()
    
    port