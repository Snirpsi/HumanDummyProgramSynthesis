#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or returns a list of words. """    
    import sys
    ports = []
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = ports + list(get_ports())
        else:
            ports.append(arg)
    print(ports)
    
<|/ file filename=ports.py source=github |>