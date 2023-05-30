#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or returns numbers. """    
    
    ports = []
    
    # Open ports
    for port in range(1, 65535):
        ports.append(port)
    
    # Return numbers
    return ports
    
