#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port and converts all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    port_to_