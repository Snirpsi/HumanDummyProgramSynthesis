#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and adds numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports.sort()
    
    for port in ports:
        