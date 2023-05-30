#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    # Open ports
    ports = openPorts()
    
    # Convert ports
    ports.convert()
    
    # Close ports
    ports.close()
    
    # Print results
    print("Ports converted")
    
