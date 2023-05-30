#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or enumerates all ports. """    
    ports = enumerate_ports()
    for port in ports:
        open_port(port)
        
<|/ file filename=ports.py source=github |>