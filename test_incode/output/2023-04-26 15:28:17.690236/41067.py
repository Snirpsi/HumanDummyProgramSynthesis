#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or opens a port. """    
    
    ports = []
    
    # Open the port and enumerate all ports
    ports.append(open("/dev/ttyUSB0"))
    ports.append(open("/dev/ttyUSB1"))
    ports.append(open("/dev/ttyUSB2"))
    
    # Enumerate all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close the port and exit
    ports[0].close()
    port