#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or opens user input. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    ports_open = False
    
    for port in ports:
        if port == "open":
            ports_open = True
        else:
            