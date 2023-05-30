#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and prints a list of numbers. """    
    
    ports = [int(i) for i in open("ports.txt").read().split()]
    
    print("\n".join(map(str, ports)))
    
