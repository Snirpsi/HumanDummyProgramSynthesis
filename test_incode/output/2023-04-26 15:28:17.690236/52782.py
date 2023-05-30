#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    import sys
    ports = sys.argv[1:]
    for port in ports:
        port = int(port)
        port