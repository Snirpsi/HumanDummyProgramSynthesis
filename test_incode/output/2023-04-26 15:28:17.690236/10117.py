#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports. """    
    
    ports = []
    
    # Open all ports
    for port in range(1,65535):
        ports.append(port)
    
    # Close all ports
    for port in range(1,65535):
        ports.append(port)
    
    # Print all ports
    for port in ports:
        print(port)
        
    # Close all ports
    for port in ports:
        port.close()
        
    # Close all ports
    for port in ports:
        port.