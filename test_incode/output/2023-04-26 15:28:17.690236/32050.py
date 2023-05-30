#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and calculates all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        webserver.