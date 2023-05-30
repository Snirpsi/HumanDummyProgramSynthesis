#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and enumerates words. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        
        port_name = port
        
        port_file = open(port_name, 'r')
        
        words = port_file.read().splitlines()
        
        for word in words:
            
            print(word)
            
        port_file.close()
        
