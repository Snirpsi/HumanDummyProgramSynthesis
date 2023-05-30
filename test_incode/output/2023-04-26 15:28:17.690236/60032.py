#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers or returns a port. """    
    import sys
    port = int(sys.argv[1])
    
    # Enumerate ports
    for port in range(port, 65535):
        print(port)
    
    # Return port
    return port
