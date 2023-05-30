#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers and removes all ports. """    
    ports = input("Enter ports: ")
    ports = ports.split()
    ports = [int(i) for i in ports]
    ports = [i for i in ports if i not in range(0,65535)]
    ports = list(set(ports))
    ports.sort()
    ports = " ".join(str(i) for i in ports)
    print(ports)

<|/ file source=github ext=.py |>