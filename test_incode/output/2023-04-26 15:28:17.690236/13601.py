#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or returns all ports. """    
    ports = []
    
    for port in ports:
        
        if port.is_open():
            
            port.close()
            
        else:
            
            port.open()
            
            ports.append(port)
            
    return ports
