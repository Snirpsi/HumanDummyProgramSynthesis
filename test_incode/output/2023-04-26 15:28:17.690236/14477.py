#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = enumerate()
    
    for port, desc in ports:
        print("%-25s %s" % (port, desc))
    
