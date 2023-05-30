#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and iterates over all ports. """    
    ports = sys.argv[1:]
    for port in ports:
        remove_ports(port)
        
<|/ file filename=remove_ports.py ext=.py |>