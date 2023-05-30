#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input and opens all ports. """    
    ports = openPorts()
    
    # Print the ports found
    for port in ports:
        print(port)
    
    # Close the ports
    for port in ports:
        port.close()
    
    # Close the program
    sys.exit(0)
    
