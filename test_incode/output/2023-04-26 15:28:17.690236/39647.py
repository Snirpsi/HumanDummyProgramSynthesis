#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or iterates over a port. """    
    ports = openports()
    for port in ports:
        process_port(port)
    
<|/ file ext=.py source=github |>