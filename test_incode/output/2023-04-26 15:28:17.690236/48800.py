#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or prints all ports. """    
    ports = input("Enter ports separated by spaces (ex: 1234 4567): ")
    ports = ports.split()
    ports = map(int, ports)
    ports = list(ports)
    ports.sort()
    for port in ports:
        print(port)
    
<|/ file source=github filename=ports.py |>