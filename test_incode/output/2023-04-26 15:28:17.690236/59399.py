#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers or returns all ports. """    
    ports = []
    
    # Open ports
    ports = openPorts(ports)
    
    # Print ports
    print(ports)
    
    # Close ports
    ports.close()
    
    # Close program
    sys.exit(0)
    
