#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and prints all ports. """    
    ports = enumerate_ports()
    for port in ports:
        print(port)
        
    
<|/ file filename=enumerate_ports.py ext=.py |>