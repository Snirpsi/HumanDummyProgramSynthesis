#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and returns all ports. """    
    ports = []
    for port in range(1,65535):
        ports.append(port)
    return ports

<|/ file filename=ports.py source=github |>