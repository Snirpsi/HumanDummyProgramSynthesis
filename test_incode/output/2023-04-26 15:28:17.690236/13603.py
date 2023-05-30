#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    for port in ports:
        open_port(port)

<|/ file source=github ext=.py filename=open_ports.py |>