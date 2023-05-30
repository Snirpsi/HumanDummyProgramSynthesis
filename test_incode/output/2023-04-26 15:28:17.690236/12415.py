#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or opens all ports. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        