#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    ports = Ports()
    for port in ports.ports:
        port.run()
        
    
<|/ file source=github ext=.py |>