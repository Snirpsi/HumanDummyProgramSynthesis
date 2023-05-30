#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port and iterates over all ports. """    
    
    ports = Ports()
    ports.calculate_ports()
    
    ports.print_ports()
    
    ports.print_port_details()
    
    ports.print_port_details_