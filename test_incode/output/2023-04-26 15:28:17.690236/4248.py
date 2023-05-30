#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and opens a port. """    
    
    ports = openPorts()
    
    for port in ports:
        port.close()
    
    
