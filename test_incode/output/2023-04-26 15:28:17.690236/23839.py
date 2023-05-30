#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers and enumerates all ports. """    
    
    # Add ports
    ports = add_ports()
    
    # Enumerate ports
    ports = enumerate_ports(ports)
    
    # Print ports
    print_ports(ports)
    
    # Print all ports
    print_all_ports(ports)
    
    # Print all ports except the first
    print_all_ports(ports[1:])
    
    # Print all ports except the last
    print_all_ports(ports[:-1]