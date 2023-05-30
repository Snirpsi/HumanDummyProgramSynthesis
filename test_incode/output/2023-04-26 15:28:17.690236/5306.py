#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or calculates all ports. """    
    ports = input('Enter the ports separated by comma: ')
    ports = ports.split(',')
    ports = list(map(int, ports))
    ports.sort()
    return ports

<|/ file source=github ext=.py |>