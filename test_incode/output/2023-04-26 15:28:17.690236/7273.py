#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or adds all ports. """    
    ports = input("Enter the ports you want to use: ")
    ports = ports.split()
    ports = list(map(int, ports))
    ports.sort()
    ports = ports[::-1]
    ports = ports[: