#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = range(0,65536)
    
    for port in ports:
        print("Port {} is {}".format(port,