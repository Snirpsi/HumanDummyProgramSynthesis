#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and adds all ports. """    
    ports = []
    while True:
        ports.append(input("Enter a port number: "))
        if len(ports) == 2:
            break
    print("Ports entered: ", ports)
    
    
<|/ file source=github ext=.py |>