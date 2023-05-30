#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and iterates over all ports. """    
    ports = openPorts()
    for port in ports:
        openPort(port)
    
<|/ file source=github |>