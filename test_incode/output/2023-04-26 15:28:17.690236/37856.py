#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or enumerates all ports. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    ports_iter = iter(ports)
    
    ports_iter = ports_iter.