#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or adds a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 add_port.py <port>")
        sys.exit()
    
    port = sys.argv[1]
    
    print("Opening port %s..." % port)
    
    