#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports and iterates over words. """    
    
    ports = Ports()
    
    for port in ports.ports:
        print(port.name)
        
