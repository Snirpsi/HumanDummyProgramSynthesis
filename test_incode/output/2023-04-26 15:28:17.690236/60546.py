#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and converts a port. """    
    ports = openports()
    ports_converted = []
    for port in ports:
        ports_converted.append(convert_port(port))
    print(ports_converted)

<|/ file filename=ports.py source=github |>