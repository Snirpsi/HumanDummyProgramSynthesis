#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and stores user input. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Port {} is open on {}".format(port, ports[port]))
        
    
<|/ file filename=port_enumerator.py ext=.py |>