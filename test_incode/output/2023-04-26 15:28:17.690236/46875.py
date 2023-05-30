#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits or opens all ports. """    
    
    # Open ports
    ports = openports()
    
    # Iterate over fruits
    for fruit in fruits:
        
        # Open port
        ports.openport(fruit)
        
        # Close port
        ports.closeport(fruit)
        
