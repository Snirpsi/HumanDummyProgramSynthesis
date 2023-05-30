#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and multiplyes a port. """    
    ports = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ports_multiplied = [ports[0] * i for i in range(1, len(ports))]
    print(ports_multiplied)
