#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or returns all ports. """    
    ports = input("Enter ports: ").split()
    ports = [int(p) for p in ports]
    return ports

<|/ file ext=.py filename=ports.py |>