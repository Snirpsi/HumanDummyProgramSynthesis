#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or stores numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports_sum = sum(ports)
    
    for port in ports:
        