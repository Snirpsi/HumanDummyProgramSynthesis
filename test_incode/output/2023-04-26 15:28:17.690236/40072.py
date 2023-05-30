#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or prints all ports. """    
    while True:
        ports = input("Enter ports: ")
        ports = ports.split()
        for port in ports:
            print(port)
