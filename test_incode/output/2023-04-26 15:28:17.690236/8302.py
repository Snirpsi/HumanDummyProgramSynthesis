#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or opens all ports. """    
    
    # Get the ports we want to open
    ports = sys.argv[1:]
    
    # Open the ports
    openports(ports)
    
