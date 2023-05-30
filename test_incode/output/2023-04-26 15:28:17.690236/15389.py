#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or converts a port. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = range(1,65535)
    
    for port in ports:
        convert_port(port)
    
