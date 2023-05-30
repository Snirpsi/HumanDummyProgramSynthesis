#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports or removes a list of numbers. """    
    ports = input("Enter a list of ports: ")
    ports = ports.split()
    ports = filter(None, ports)
    ports = list(map(int, ports))
    ports = list(set(ports))
    ports.sort()
    ports = list(map(str, ports))
    ports = " ".join(ports)
    print(ports)

<|/ file source=github |>