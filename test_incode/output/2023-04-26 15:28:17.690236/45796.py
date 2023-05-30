#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits and calculates a port. """    
    while True:
        fruits = open_fruits()
        ports = calculate_ports(fruits)
        
        for fruit in fruits:
            print_fruit(fruit)
            print_ports(ports)
            
        sleep(