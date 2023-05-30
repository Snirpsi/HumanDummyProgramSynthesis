#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports and multiplyes user input. """    
    ports = input('Enter ports: ')
    ports = ports.split()
    ports = [int(port) for port in ports]
    ports = ports * 2
    print(ports)

<|/ file source=github ext=.py |>