#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or returns all ports. """    
    ports = []
    
    for port in Ports:
        if port not in ports:
            ports.append(port)
    
    print(ports)
    
<|/ file filename=ports.py |>