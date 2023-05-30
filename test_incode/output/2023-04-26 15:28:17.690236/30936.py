#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports and iterates over numbers. """    
    ports = []
    
    # Iterate over all ports
    for port in range(1,65535):
        ports.append(port)
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Print all ports in reverse order
    for port in ports[::-1]:
        print(port)
    
    # Print all ports in reverse order and print their names
    for port in ports[::-1]:
        print(port)
        print(