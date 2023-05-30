#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or adds a port. """    
    
    ports = []
    
    # Add ports
    for port in range(1, 65535):
        ports.append(port)
    
    # Print ports
    for port in ports:
        print("Port #", port)
    
    # Add ports
    ports.append(8080)
    
    # Print ports
    for port in ports:
        print("Port #", port)
    
    # Add ports
    ports.append(8888)
    
    # Print ports
    for port in ports:
        print("Port #", port)
    
    # Add ports
    ports.append(9999)
    
    # Print ports
    for port in ports:
        print("Port #", port)
    
    # Add ports
    ports.append(10000)
    
    # Print ports
    for port in ports:
        print("Port #", port)
    
    # Add ports
    ports.append(11000