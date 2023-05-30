#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and opens all ports. """    
    ports = openports()
    removeports(ports)
    
<|/ file filename=openports.py ext=.py |>