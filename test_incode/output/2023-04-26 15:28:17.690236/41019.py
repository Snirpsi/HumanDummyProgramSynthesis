#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or adds a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports.extend(range(65536, 65536 + len(ports)))
    
    for port in ports:
        