#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports or stores numbers. """    
    while True:
        ports = [int(i) for i in input().split()]
        for port in ports:
            print(port * 