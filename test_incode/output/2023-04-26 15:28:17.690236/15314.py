#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = [x*y for x, y in zip(ports, ports)]
    print('\n'.join(str(p) for p in ports))
    
<|/ file source=github ext=.py |>