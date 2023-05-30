#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports and removes all ports. """    
    
    ports = find_ports()
    
    for port in ports:
        remove_port(port)
    
    print("Done.")

<|/ file source=github filename=remove_ports.py |>