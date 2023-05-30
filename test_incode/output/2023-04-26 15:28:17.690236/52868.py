#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and enumerates numbers. """    
    
    port = int(sys.argv[1])
    
    for port in range(port, 65535):
        print(port)
    
