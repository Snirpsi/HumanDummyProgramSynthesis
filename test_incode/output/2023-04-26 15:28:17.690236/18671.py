#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or iterates over all ports. """    
    
    # Initialize and add ports
    ports = Ports()
    ports.add_ports()
    
    # Iterate over all ports
    for port in ports:
        print(port)
        
