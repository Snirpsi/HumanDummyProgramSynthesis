#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or returns all ports. """    
    ports = openPorts()
    
    for port in ports:
        print(port)
    
    
<|/ file source=github filename=ports.py |>