#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or prints a list of numbers. """    
    ports = [int(i) for i in input("Enter ports separated by comma: ").split(',')]
    for port in ports:
        print(port)
    
