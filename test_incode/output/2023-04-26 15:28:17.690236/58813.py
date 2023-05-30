#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or returns all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = range(1,65535)
    
    for port in ports:
        print("Port %i: %s" % (port, 