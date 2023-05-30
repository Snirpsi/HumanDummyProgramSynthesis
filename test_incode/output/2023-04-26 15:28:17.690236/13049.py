#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or enumerates all ports. """    
    
    # Get the ports
    ports = listPorts()
    
    # Print the ports
    print("Ports:")
    for port in ports:
        print("  {}: {}".format(port, listPort