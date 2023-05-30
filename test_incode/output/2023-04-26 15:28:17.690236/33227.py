#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and removes all ports. """    
    ports = input("Enter the ports separated by commas: ")
    ports = ports.split(",")
    ports = [port.strip() for port in ports]
    ports = [port for port in ports if port]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(ports)
    print(ports)

<|/ file filename=ports.py source=github |>