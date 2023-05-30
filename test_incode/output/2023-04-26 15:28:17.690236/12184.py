#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports. """    
    
    # Read input file
    ports = read_ports()
    
    # Calculate all ports
    ports_all = []
    for port in ports:
        ports_all.append(ports[port])
        
    # Calculate all ports percentages
    ports_percentages = []
    for port in ports_all:
        ports_percentages.append(ports[port] / ports_all