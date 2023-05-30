#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or multiplyes a list of words. """    
    import sys
    ports = []
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    ports = ports * 2
    print(ports)
    
<|/ file ext=.py |>