#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores all ports and enumerates all ports. """    
    
    # Get the ports 
    ports = Ports()
    
    # Enumerate the ports
    ports.enumerate()
    
    # Print the ports
    ports.print_ports()
    
    # Print the ports names
    ports.print_ports_names()
    
    # Print the ports names
    ports.print_ports_names(