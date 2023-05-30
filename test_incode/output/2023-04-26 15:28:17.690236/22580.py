#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or converts a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    
    if len(sys.argv) > 2:
        ports = sys.argv[2:]
    else:
        ports = range(port)
    
    for port in ports:
        