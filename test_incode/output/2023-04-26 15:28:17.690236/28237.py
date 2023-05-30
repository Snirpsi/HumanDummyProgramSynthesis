#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and enumerates a list of numbers. """    
    ports = enumerate_ports()
    ports_str = ",".join(str(p) for p in ports)
    print(ports_str)
    
<|/ file source=github |>