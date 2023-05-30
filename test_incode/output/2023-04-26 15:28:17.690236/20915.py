#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and removes a port. """    
    ports = input("Enter the ports separated by commas: ")
    ports = ports.split(",")
    for port in ports:
        ports.remove(port)
    print(ports)
