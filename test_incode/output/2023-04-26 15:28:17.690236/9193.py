#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports. """    
    while True:
        ports = [int(x) for x in input().split()]
        ports.sort()
        ports.reverse()
        for port in ports:
            print(port)
            
