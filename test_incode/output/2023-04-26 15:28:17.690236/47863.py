#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or adds all ports. """    
    ports = enumerate_ports()
    
    # Print the list of ports
    for port in ports:
        print(port)
        
    # Add all ports
    add_ports(ports)
    
