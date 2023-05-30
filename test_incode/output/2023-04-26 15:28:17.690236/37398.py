#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and converts a list of numbers. """    
    port = int(sys.argv[1])
    
    ports = [int(p) for p in sys.argv[2:]]
    
    ports.sort()
    
    for port in ports:
        