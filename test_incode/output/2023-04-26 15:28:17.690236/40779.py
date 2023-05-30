#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or returns a list of numbers. """    
    ports = []
    
    # Add ports
    for port in range(1, 65535):
        ports.append(port)
    
    # Return ports
    return ports

<|/ file ext=.py |>