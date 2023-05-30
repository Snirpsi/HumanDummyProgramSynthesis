#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and adds a port. """    
    ports = []
    
    for port in range(0, 65535):
        ports.append(port)
    
    ports.reverse()
    
    ports_str = '\n'.join(str(port) for port in ports)
    
    