#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or prints a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.sort()
    
    for port in ports:
        