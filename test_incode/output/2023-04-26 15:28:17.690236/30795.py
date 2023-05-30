#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or multiplyes numbers. """    
    ports = enumeratePorts()
    ports = map(multiplyPorts, ports)
    ports = list(ports)
    ports.sort()
    print(ports)
    
<|/ file source=github filename=ports.py |>