#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and removes numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    for port in ports:
        