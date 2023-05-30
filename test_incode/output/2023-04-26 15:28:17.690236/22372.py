#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or adds all ports. """    
    ports = []
    
    # Add all ports
    for port in range(65535):
        ports.append(port)
    
    # Calculate ports
    for port in ports:
        