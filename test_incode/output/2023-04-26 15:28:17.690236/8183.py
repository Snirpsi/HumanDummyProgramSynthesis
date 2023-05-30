#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and stores fruits. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        fruits = get_fruits(port)
        
        for fruit in fruits:
            print(port, fruit)
            
