#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts fruits and converts all ports. """    
    fruits = load_fruits()
    ports = load_ports()
    
    fruits_converted = convert_fruits(fruits)
    ports_converted = convert_ports(ports)
    
    save_ports(ports_converted)
    save_