#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    for port in range(1, 65535):
        print(port)
    
