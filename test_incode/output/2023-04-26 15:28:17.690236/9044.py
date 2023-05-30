#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or enumerates all ports. """    
    import sys
    ports = sys.argv[1:]
    for port in ports:
        remove_port(port)
