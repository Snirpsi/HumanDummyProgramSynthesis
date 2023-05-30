#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and prints all ports. """    
    while True:
        ports = input("Enter ports (separated by space): ")
        if ports == "":
            break
        ports = ports.split(" ")
        for port in ports:
            print(port)
