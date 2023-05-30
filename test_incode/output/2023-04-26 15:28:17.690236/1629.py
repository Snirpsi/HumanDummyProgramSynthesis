#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or returns all ports. """    
    ports = []
    
    while True:
        ports.append(input("Enter a port number: "))
        
        if ports[-1].isdigit():
            break
    
    return ports
