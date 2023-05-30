#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or enumerates all ports. """    
    import sys
    
    if len(sys.argv) == 1:
        ports = range(1,65535)
    else:
        ports = sys.argv[1:]
    
    for port in ports:
        print("Port {}: {}".format(port, 