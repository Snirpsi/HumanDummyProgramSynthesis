#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports and multiplyes all ports. """    
    
    ports = calculate_ports()
    
    for port in ports:
        ports[port] = ports[port] * 