#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and calculates a port. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        
        print("Port {} is {} ({})".format(port, ports[port][0], ports[port][1]))
        
