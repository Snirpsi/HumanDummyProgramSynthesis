#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or calculates all ports. """    
    
    ports = []
    
    # Open ports
    for port in range(0, 65535):
        ports.append(port)
        
    # Open all ports
    for port in ports:
        