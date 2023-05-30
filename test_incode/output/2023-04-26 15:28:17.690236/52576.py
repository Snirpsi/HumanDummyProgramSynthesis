#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports and removes a list of numbers. """    
    ports = enumerate_ports(sys.argv[1])
    remove_ports(ports, sys.argv[2])
    
