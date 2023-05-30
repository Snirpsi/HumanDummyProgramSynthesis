#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and prints a list of numbers. """    
    ports = []
    for port in range(1, 65535):
        ports.append(port)
    print('\n'.join(str(port) for port in ports))

<|/ file source=github filename=ports.py |>