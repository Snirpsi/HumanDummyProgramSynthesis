#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and adds all ports. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        print(port)
        
