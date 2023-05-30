#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or calculates a port. """    
    import sys
    port = int(sys.argv[1])
    
    if port == -1:
        port = find_port()
    
    port_converter(port)
    
    
<|/ file source=github ext=.py |>