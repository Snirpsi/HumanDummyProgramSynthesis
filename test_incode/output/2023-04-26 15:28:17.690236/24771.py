#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port and returns all ports. """    
    
    ports = []
    
    ports.append( get_port() )
    ports.append( get_port() )
    ports.append( get_port() )
    
    for port in ports:
        print(port)
    
    
<|/ file filename=ports.py ext=.py |>