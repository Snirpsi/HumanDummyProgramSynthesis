#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Enumerating port {}".format(port))
        
        enumerate_ports(port)
        
    print("Done.")

<|/ file source=github ext=.py |>