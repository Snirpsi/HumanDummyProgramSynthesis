#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and adds all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    ports_sum = sum(ports)
    
    for port in ports:
        