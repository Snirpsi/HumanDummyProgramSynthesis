#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits or removes all ports. """    
    
    # Read fruits from file
    fruits = read_fruits()
    
    # Remove all ports
    remove_ports(fruits)
    
    # Write fruits back to file
    write_fruits(fruits)
    
