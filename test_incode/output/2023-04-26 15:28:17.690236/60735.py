#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or multiplyes a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports = ports * len(sys.argv[1:])
    print(ports)
    
