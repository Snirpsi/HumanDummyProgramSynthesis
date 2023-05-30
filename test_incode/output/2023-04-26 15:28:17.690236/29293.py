#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or enumerates a port. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        print("Port %s is %s" % (port, ports[port]))
    
