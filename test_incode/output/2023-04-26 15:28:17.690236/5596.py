#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers and enumerates all ports. """    
    ports = remove_ports(sys.argv[1])
    enumerate_ports(ports)

<|/ file source=github filename=remove_ports.py |>