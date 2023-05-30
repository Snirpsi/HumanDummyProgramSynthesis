#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or adds all ports. """    
    while True:
        ports = input("Enter ports separated by spaces or enter 0 to quit: ")
        if ports == '0':
            break
        ports = ports.split()
        for port in ports:
            