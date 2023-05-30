#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and calculates all ports. """    
    while True:
        fruits = remove_fruits()
        ports = calculate_ports(fruits)
        
        