#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Port {} is {}".format(port, ports[port]))
    
    print("Done!")

<|/ file ext=.py filename=enumerate_ports.py |>