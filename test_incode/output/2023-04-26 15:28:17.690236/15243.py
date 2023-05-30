#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers or multiplyes all ports. """    
    ports = [int(i) for i in input("Enter ports: ").split()]
    while True:
        ports = [p*n for p,n in zip(ports,ports[1:])]
        print(",".join(map(str,ports)))
