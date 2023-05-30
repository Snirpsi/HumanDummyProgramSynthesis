#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or returns all ports. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    ports = list(map(int, ports))
    ports.sort()
    print(ports)
