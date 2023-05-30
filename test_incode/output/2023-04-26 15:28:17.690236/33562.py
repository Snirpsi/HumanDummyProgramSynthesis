#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and removes user input. """    
    ports = find_ports()
    ports_remove = remove_ports(ports)
    ports_remove = ports_remove.split()
    print(ports_remove)
    
<|/ file source=github ext=.py |>