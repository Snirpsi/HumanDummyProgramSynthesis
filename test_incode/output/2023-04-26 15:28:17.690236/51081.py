#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports and converts numbers. """    
    ports = input("Enter the ports separated by comma: ").split(',')
    ports = [int(p) for p in ports]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = [p for p in ports if p > 65535]
    ports = [p for p in ports if p != 0]
    ports = [p for p in ports if p != 65535]
    ports = [p for p in ports if p != 65536]
    ports = [p for p in ports if p != 65537]
    ports = [p for p in ports if p != 65538]
    ports = [p for p in ports if p != 65539]
    ports = [p for p in ports if p != 655