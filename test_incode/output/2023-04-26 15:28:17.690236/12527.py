#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = [
        port for port in get_ports()
        if port.is_open()
    ]
    
    for port in ports:
        port.open()
        port.close()
        
    