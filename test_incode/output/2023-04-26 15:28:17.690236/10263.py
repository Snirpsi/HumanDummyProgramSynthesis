#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or adds a port. """    
    
    port = int(sys.argv[1])
    
    ports = [int(port) for port in range(1024)]
    
    ports_iter = iter(ports)
    
    for port in ports_iter:
        
        