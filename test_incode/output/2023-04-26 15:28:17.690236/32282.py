#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or enumerates all ports. """    
    ports = []
    ports = ports + listPorts()
    ports.sort()
    print(ports)
    
<|/ file filename=ports.py |>