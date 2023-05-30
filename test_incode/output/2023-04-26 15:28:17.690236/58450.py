#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or removes all ports. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(',')
    ports = [int(p) for p in ports]
    ports.sort()
    print(ports)
    
