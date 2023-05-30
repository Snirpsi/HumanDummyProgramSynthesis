#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and returns fruits. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        
        fruits = get_fruits(port)
        
        print('Port:', port, 'Fruits:', fruits)
    
