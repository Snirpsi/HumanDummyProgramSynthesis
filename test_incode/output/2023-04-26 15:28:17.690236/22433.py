#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or enumerates all ports. """    
    
    ports = find_ports()
    
    for port in ports:
        print(port)
        
    
