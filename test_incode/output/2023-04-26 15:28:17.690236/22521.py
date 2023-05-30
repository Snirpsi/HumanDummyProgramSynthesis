#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    # Get the list of ports
    ports = enumeratePorts()
    
    # Print the list of ports
    for port in ports:
        print(port)
        
    # Print the list of ports 