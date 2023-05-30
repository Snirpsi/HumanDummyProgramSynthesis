#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and prints user input. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    for port in ports:
        port = int(port)
        print(port)
