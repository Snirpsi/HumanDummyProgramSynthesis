#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python store_port.py <port>")
        sys.exit()
    
    port = sys.argv[1]
    
    store_port(port)
    
