#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port and prints all ports. """    
    
    ports = []
    
    ports.append( openPort() )
    ports.append( openPort() )
    ports.append( openPort() )
    
    for port in ports:
        port.close()
    
    
<|/ file ext=.py |>