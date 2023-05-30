#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and calculates all ports. """    
    
    ports = openPorts()
    
    for port in ports:
        
        portData = ports[port]
        
        portData[port] = portData[port].