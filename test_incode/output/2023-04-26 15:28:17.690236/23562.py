#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        