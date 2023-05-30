#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Port", port, "is", ports[port])
        
    print("All ports enumerated")

<|/ file filename=ports.py ext=.py |>