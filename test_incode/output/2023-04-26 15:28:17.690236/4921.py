#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and stores user input. """    
    ports = enumerate_ports()
    
    # Print the list of ports
    for port in ports:
        print("Port {}: {}".format(port, ports[port]))

<|/ file source=github ext=.py |>