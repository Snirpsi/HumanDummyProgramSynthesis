#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and converts all ports. """    
    ports = find_ports()
    ports_str = ','.join(ports)
    print(ports_str)

<|/ file source=github filename=ports.py |>