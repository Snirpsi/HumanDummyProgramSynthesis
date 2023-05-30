#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or returns all ports. """    
    ports = []
    while True:
        ports.append(input("Enter a port number: "))
        if ports[-1] == "":
            break
    print("Ports found:", ports)
    
<|/ file ext=.py filename=port