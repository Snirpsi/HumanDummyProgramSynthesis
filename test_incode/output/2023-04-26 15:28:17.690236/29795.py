#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports and multiplyes a port. """    
    ports = [int(i) for i in input().split()]
    ports[0] *= 2
    print(ports)
    
