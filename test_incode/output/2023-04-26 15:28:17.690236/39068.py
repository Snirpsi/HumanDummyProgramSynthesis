#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words or adds all ports. """    
    
    ports = []
    
    while True:
        port = input("Enter a port number: ")
        ports.append(port)
        
        if len(ports) == 