#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and enumerates all ports. """    
    
    port = int(sys.argv[1])
    
    ports = enumeratePorts(port)
    
    for port in ports:
        print(port)

<|/ file filename=ports.py ext=.py |>