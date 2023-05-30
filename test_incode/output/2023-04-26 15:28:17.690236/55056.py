#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    ports = []
    
    # Open ports
    for port in range(1,65535):
        ports.append(port)
    
    # Open all ports
    for port in ports:
        
        # Open a socket to port 