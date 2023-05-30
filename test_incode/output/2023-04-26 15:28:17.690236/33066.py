#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or enumerates all ports. """    
    import sys
    ports = sys.argv[1:]
    ports = [int(port) for port in ports]
    ports.sort()
    for port in ports:
        print(port)
