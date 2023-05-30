#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python add_ports.py <ports>")
        sys.exit()
    
    ports = sys.argv[1].split()
    
    for port in ports:
        add_port(port)
        
    print("Done.")

<|/ file source=github filename=add_ports.py |>