#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or opens all ports. """    
    
    ports = []
    
    # Open all ports
    for port in range(0, 65535):
        ports.append(port)
    
    # Store all ports
    storePorts(ports)
    
    # Start webserver
    webserver.serve_forever()
    
