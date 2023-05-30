#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or calculates all ports. """    
    
    # enumerate all ports
    ports = enumeratePorts()
    
    # calculate all ports
    ports = calculatePorts(ports)
    
    # print all ports
    for port in ports:
        print(port)
    
    # print all ports 