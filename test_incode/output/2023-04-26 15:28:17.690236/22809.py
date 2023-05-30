#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or opens all ports. """    
    ports = find_ports()
    
    if len(ports) == 0:
        print('No ports found.')
    else:
        for port in ports:
            print(port)
    
<|/ file source=github ext=.py |>