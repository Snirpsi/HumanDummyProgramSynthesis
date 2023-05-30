#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and multiplyes user input. """    
    ports = input("Enter the ports seperated by comma: ")
    ports = ports.split(",")
    ports = [int(p) for p in ports]
    ports = [p*2 for p in ports]
    ports = ",".join(str(p) for p in ports)
    print(ports)

<|/ file source=github ext=.py |>