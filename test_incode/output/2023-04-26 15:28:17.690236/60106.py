#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or iterates over all ports. """    
    ports = input("Enter the port numbers (separated by commas): ")
    ports = ports.split(",")
    for port in ports:
        print(port)
