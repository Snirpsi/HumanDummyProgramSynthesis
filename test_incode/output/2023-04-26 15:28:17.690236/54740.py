#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or converts all ports. """    
    
    ports = [int(i) for i in input("Enter ports: ").split()]
    
    ports_converted = [str(int(i)) for i in ports]
    
    print(ports_converted)
<|/ file source=github ext=.py |>