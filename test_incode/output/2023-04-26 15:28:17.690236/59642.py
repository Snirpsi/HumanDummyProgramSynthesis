#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports. """    
    while True:
        ports = [int(i) for i in input("Enter ports separated by spaces (1-65535): ").split()]
        ports.sort()
        ports = list(ports)
        ports.reverse()
        ports = [str(p) for p in ports]
        ports.sort()
        for p in ports:
            print(p)
        
