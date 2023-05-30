#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and adds a port. """    
    
    port = int(sys.argv[1])
    
    ports = range(port)
    
    ports_str = ','.join(ports)
    
    