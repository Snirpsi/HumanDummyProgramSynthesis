#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print(port)
        
