#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and enumerates all ports. """    
    
    ports = listPorts()
    
    while True:
        
        # Remove all ports
        for port in ports:
            
            # Remove port
            removePort(port)
            
        # Enumerate all ports
        ports = listPorts()
        
        # Sleep for one second
        time.sleep(1)
        
