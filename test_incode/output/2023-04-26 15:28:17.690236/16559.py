#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and multiplyes a port. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        port_number = port
        
        port_number = port_number * port
        
        print(port_number)
        
    
