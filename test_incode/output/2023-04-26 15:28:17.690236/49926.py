#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    ports = enumerate_ports()
    
    print("\nPorts:")
    for port in ports:
        print("\t", port)
    
    
<|/ file ext=.py |>