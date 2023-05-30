#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_port.py <port>")
        sys.exit()
    
    port = sys.argv[1]
    
    remove_port(port)
    
