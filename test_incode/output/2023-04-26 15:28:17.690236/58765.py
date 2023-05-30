#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or stores a list of numbers. """    
    ports = [int(x) for x in input("Enter a port number: ").split()]
    ports.sort()
    print("\nPorts:")
    for port in ports:
        print("\t", port)
    
<|/ file filename=ports.py source=github ext=.py |>