#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 remove_port.py <port>")
        exit(1)
    
    port = sys.argv[1]
    
    remove_port(port)
    
