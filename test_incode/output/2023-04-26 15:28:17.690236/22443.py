#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports. """    
    
    # Load all ports
    ports = load_ports()
    
    # Calculate all ports
    ports_all = calculate_ports(ports)
    
    # Print all ports
    print_ports(ports_all)
    
    # Print all ports 