#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and opens all ports. """    
    ports = range(1,65535)
    for port in ports:
        openport(port)
        
<|/ file ext=.py |>