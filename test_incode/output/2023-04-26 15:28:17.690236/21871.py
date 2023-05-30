#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    ports = find_ports()
    for port in ports:
        run(port)
        
<|/ file ext=.py |>