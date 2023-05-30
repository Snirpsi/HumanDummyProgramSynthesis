#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and converts user input. """    
    
    # Open ports
    ports = openports()
    
    # Convert user input
    ports_converted = ports_converter(ports)
    
    # Print result
    print(ports_converted)
    
