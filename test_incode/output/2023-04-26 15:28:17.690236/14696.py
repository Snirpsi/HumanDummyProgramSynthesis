#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or stores words. """    
    
    while True:
        
        ports = Ports()
        
        for port in ports.ports:
            
            ports.ports[port].calculate(ports.ports[port].ports)
            
        ports.ports.