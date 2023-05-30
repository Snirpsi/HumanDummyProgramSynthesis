#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or returns all ports. """    
    ports = []
    while True:
        ports.append(input("Enter a port number: "))
        if len(ports) == 2:
            break
    return ports

<|/ file filename=port