#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or opens all ports. """    
    
    ports = openPorts()
    
    for port in ports:
        port.open()
        
    
