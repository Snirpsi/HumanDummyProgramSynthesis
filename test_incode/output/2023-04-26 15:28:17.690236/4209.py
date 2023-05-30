#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input and removes all ports. """    
    ports = input("Enter ports separated by comma: ").split(',')
    for port in ports:
        ports.remove(port)
    return ports

<|/ file source=github filename=ports.py |>