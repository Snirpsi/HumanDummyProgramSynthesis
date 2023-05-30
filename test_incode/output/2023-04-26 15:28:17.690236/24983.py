#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or converts all ports. """    
    import sys
    port = int(sys.argv[1])
    
    # Iterate over all ports
    for port in range(1,65535):
        print("Port {}: 