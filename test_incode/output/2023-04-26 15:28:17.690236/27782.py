#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or returns all ports. """    
    while True:
        ports = input("Enter ports separated by comma: ").split(',')
        if ports:
            ports = [int(p) for p in ports]
            ports.sort()
            print(ports)
        else:
            break
    
