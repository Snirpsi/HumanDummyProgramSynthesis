#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or removes all ports. """    
    while True:
        ports = input("Enter ports separated by commas: ")
        ports = ports.split(",")
        for port in ports:
            print(port)
