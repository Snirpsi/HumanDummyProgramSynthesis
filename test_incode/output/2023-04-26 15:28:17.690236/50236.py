#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and stores all ports. """    
    ports = openPorts()
    
    for port in ports:
        openPort(port)
    
    
<|/ file ext=.py source=github filename=ports.py |>