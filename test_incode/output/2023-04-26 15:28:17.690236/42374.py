#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or enumerates user input. """    
    ports = input("Enter ports separated by spaces (no spaces allowed): ")
    ports = ports.split()
    for port in ports:
        print(port)
    
