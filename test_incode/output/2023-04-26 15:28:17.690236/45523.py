#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    while True:
        port = ports.pop()
        
        if port is not None:
            remove_port(port)
        else:
            break
        
    
