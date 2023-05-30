#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and returns a list of numbers. """    
    ports = openPorts()
    ports.sort()
    for port in ports:
        print(port)
    
<|/ file source=github filename=openPorts.py |>