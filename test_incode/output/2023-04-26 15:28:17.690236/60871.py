#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of numbers and converts a port. """    
    ports = [int(i) for i in input("Enter a port number: ").split()]
    ports.sort()
    ports = [ports[0]] + ports[1:]
    ports = list(map(str, ports))
    ports.sort()
    ports = ports + [''] * (ports[-1] - ports[0])
    return ports

<|/ file filename=ports.py source=github |>