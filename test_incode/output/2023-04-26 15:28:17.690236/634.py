#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports or removes a list of numbers. """    
    ports = [int(x) for x in input('Enter ports: ').split()]
    ports.remove(int(input('Enter a number: ')))
    print(ports)
    
