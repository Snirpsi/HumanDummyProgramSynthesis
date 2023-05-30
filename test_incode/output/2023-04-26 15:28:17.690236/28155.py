#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports and iterates over user input. """    
    ports = input("Enter ports separated by spaces (no quotes): ")
    ports = ports.split()
    ports = list(map(int, ports))
    
    for port in ports:
        print(port)
    
