#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or enumerates a port. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        
        port