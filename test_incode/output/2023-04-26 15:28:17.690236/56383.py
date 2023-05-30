#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or adds all ports. """    
    while True:
        ports = input("Enter ports separated by spaces (no spaces allowed): ")
        if ports == '':
            break
        ports = ports.split()
        for port in ports:
            ports.remove(port)
        print("Ports removed: ", ports)
        print("Enter ports again: ")
